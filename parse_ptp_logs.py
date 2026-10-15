import re
import argparse
import numpy as np

def parse_ptp4l_log(log_file):
    offsets = []
    path_delays = []
    
    # 匹配 LinuxPTP ptp4l 標準輸出: ptp4l[123.456]: master offset -42 s2 freq +1234 path delay 16931
    log_pattern = re.compile(r"master offset\s+(-?\d+)\s+s\d+\s+freq\s+[\+\-]?\d+\s+path delay\s+(\d+)")

    with open(log_file, "r") as f:
        for line in f:
            if "master offset" not in line:
                continue
                
            match = log_pattern.search(line)
            if match:
                offset = int(match.group(1))
                delay = int(match.group(2))
                offsets.append(offset)
                path_delays.append(delay)

    if not offsets:
        print("[!] Warning: No valid synchronization log entries found. Check log format.")
        return

    offsets_arr = np.array(offsets)
    delays_arr = np.array(path_delays)

    print("\n==========================================")
    print(" PTP Log Analysis Report (ptp4l Diagnostics)")
    print("==========================================")
    print(f"Total Log Frames Processed : {len(offsets_arr)}")
    print(f"RMS Offset                 : {np.sqrt(np.mean(offsets_arr**2)):.2f} ns")
    print(f"Max Positive / Negative    : +{np.max(offsets_arr)} / {np.min(offsets_arr)} ns")
    print(f"Mean Path Delay            : {np.mean(delays_arr):.2f} ns")
    print(f"Jitter (Offset StdDev)     : {np.std(offsets_arr):.2f} ns")
    print("==========================================\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser for LinuxPTP (ptp4l) log stats.")
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to ptp4l log file")
    args = parser.parse_args()
    parse_ptp4l_log(args.file)
