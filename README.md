# IEEE 1588 PTP Grandmaster Clock on Raspberry Pi 4

利用 Raspberry Pi 4、u-blox GPS 模組（PPS）與支援硬體時間戳記（HW Timestamping）的網卡，打造低成本、奈秒級精度的 PTP 時鐘主機[cite: 1]。

## 核心效能指標
* **同步精度**：經由 HW Timestamping + PPS 校正，時鐘偏差（Offset）穩定控制在 ±30 ns ~ ±100 ns[cite: 1]。
* **交換機延遲分析**：實測非 PTP 交換機的排隊延遲（Queueing delay），路徑延遲從 16.9 µs 暴增至 45.6 µs[cite: 1]。
* **日誌分析工具**：撰寫 Python 腳本解析 ptp4l 與 pmc 日誌，即時追蹤不同網路架構下的同步指標[cite: 1]。

## 系統架構
* **時間源**：GPS NMEA (via UART) + 1PPS (via GPIO)[cite: 1]。
* **服務堆疊**：chrony（負責 GPS/PPS 同步） → 系統時鐘 (CLOCK_REALTIME) → ptp4l（透過硬體時間戳記擔任 PTP Grandmaster）[cite: 1]。
* **監控機制**：使用 pmc 進行即時狀態追蹤[cite: 1]。

## 網路實測對比

| 網路拓撲 | 時間戳記方式 | 平均路徑延遲 (Avg Path Delay) | 時鐘偏差穩定度 (Clock Offset Stability) |
| :--- | :--- | :--- | :--- |
| **直連 (Direct Link)** | Hardware | 16.9 µs | ±30 ns ~ ±100 ns |
| **經過非 PTP 交換機** | Hardware | 45.6 µs (含 Queueing delay) | ±1,200 ns (抖動明顯) |
| **直連 (NTP 模式)** | Software | N/A | ±1.2 ms |

## 網卡檢測指令
確認網卡是否支援 PTP 硬體時間戳記[cite: 1]：

```bash
ethtool -T eth0
