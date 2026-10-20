IEEE 1588 PTP Grandmaster Clock on Raspberry Pi 4
- Designed a sub-100ns PTP Grandmaster clock by interfacing a u-blox GPS module (1PPS via GPIO) with Raspberry Pi 4 using chrony, ptp4l, and phc2sys.
- Achieved ±30ns to ±100ns clock offset over direct links by validating Ethernet HW timestamping support (ethtool -T) on the Broadcom MAC.
- Quantitative Network Analysis: Benchmarked PTP degradation across non-PTP switches, observing path delay jumps (16.9 µs → 45.6 µs) and offset variance (±100 ns → ±1,200 ns) due to queueing jitter.
- Diagnostics & Tooling: Developed custom Python log parsers to batch-extract synchronization metrics from ptp4l/pmc outputs for performance comparison.
