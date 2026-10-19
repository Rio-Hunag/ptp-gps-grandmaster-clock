# IEEE 1588 PTP Grandmaster Clock on Raspberry Pi 4

A budget-friendly, nanosecond-level PTP Grandmaster Clock using a Raspberry Pi 4, u-blox GPS module (PPS), and a hardware timestamping NIC.

## Key Achievements
* **Sync Accuracy:** Kept offset within **±30 ns to ±100 ns** using HW timestamping + PPS.
* **Switch Latency Analysis:** Measured queueing delay on non-PTP switches, showing path delay jumped from **16.9 µs to 45.6 µs**.
* **Log Parsing:** Wrote Python scripts to parse `ptp4l` and `pmc` logs for tracking sync metrics across different setups.

## System Architecture
* **Time Source:** GPS NMEA over UART + 1PPS via GPIO.
* **Daemon Stack:** `chrony` (GPS/PPS sync) → System Clock (`CLOCK_REALTIME`) → `ptp4l` (PTP Grandmaster via HW timestamping).
* **Monitoring:** `pmc` for real-time tracking.

## Benchmarking: PTP vs. Non-PTP Network

| Topology | Timestamping | Avg Path Delay | Clock Offset Stability |
| :--- | :--- | :--- | :--- |
| **Direct Link** | Hardware | 16.9 µs | ±30 ns ~ ±100 ns |
| **Non-PTP Switch** | Hardware | 45.6 µs (Queueing delay) | ±1,200 ns (Jittery) |
| **Direct Link (NTP)** | Software | N/A | ±1.2 ms |

## Diagnostics
Check if your NIC supports hardware timestamping:

```bash
ethtool -T eth0
