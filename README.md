# IEEE 1588 PTP Grandmaster Clock on Raspberry Pi 4

使用 Raspberry Pi 4、u-blox GPS 模組 (PPS) 與支援硬體時間戳記 (HW timestamping) 的 NIC 建立低成本、奈秒級精度的 PTP 時鐘主機[cite: 1]。

### Key Achievements
- Sync Accuracy: Kept offset within ±30 ns to ±100 ns using HW timestamping + PPS[cite: 1].
- Switch Latency Analysis: Measured queueing delay on non-PTP switches, showing path delay jumped from 16.9 µs to 45.6 µs[cite: 1].
- Log Parsing: Wrote Python scripts to parse ptp4l and pmc logs for tracking sync metrics across different setups[cite: 1].

### System Architecture
- Time Source: GPS NMEA over UART + 1PPS via GPIO[cite: 1].
- Daemon Stack: chrony (GPS/PPS sync) -> System Clock (CLOCK_REALTIME) -> ptp4l (PTP Grandmaster via HW timestamping)[cite: 1].
- Monitoring: pmc for real-time tracking[cite: 1].

### Benchmarking: PTP vs. Non-PTP Network

Topology | Timestamping | Avg Path Delay | Clock Offset Stability
---|---|---|---
Direct Link | Hardware | 16.9 µs | ±30 ns to ±100 ns
Non-PTP Switch | Hardware | 45.6 µs (Queueing delay) | ±1,200 ns (Jittery)
Direct Link (NTP) | Software | N/A | ±1.2 ms

### Diagnostics
Check if your NIC supports hardware timestamping[cite: 1]:

ethtool -T eth0
