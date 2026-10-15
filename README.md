# High-Precision IEEE 1588 PTP Grandmaster Clock (Raspberry Pi + GPS/PPS)

A low-cost, nanosecond-level time synchronization Grandmaster Clock built under embedded Linux using Raspberry Pi 4, u-blox GPS module (PPS signal), and IEEE 1588 Hardware Timestamping capable NIC.

## 🚀 Key Achievements & Metrics
- **Synchronization Accuracy**: Maintained Offset within **±30 ns to ±100 ns** via Hardware Timestamping + PPS.
- **Root Cause Analysis**: Identified non-PTP-aware switch queueing delay penalty (Path Delay degraded from **16,931 ns** to **45,601 ns**).
- **Tooling**: Built custom Python log parsers to analyze `ptp4l` and `pmc` synchronization logs for multi-scenario reporting.

## 🏗️ System Architecture
- **Time Source**: GPS NMEA via UART + 1PPS signal via Raspberry Pi GPIO.
- **Daemon Layer**: `chrony` (GPS/PPS reference clock) -> Linux System Time (`CLOCK_REALTIME`) -> `ptp4l` (PTP Grandmaster via HW Timestamping).
- **Monitoring**: `pmc` (PTP Management Client) for real-time state tracking.

## 📊 Root Cause Analysis: Queueing Delay in Non-PTP Network Switches
| Topology / Protocol | Hardware/Software Timestamp | Average Path Delay | Clock Offset Stability |
| :--- | :--- | :--- | :--- |
| **Direct Ethernet Link** | Hardware Timestamping | **16,931 ns** | **±30 ns ~ ±100 ns** |
| **Non-PTP Switch** | Hardware Timestamping | **45,601 ns** (Queueing Delay) | ±1,200 ns (Jittered) |
| **Direct Link (NTP)** | Software Timestamping | N/A | ±1.2 ms |

## 🛠️ How to Verify & Run Diagnostics

### 1. Check Hardware Timestamping Support on NIC
```bash
ethtool -T eth0
