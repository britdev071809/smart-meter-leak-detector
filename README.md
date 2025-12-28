# Smart Meter Leak Detector

An open-source proof-of-concept tool for detecting household water leaks from smart meter data using simple rule-based algorithms. This project demonstrates how data from smart meters can be used to identify continuous leaks (e.g., running toilets, faulty taps) through time-series analysis.

## Background

Water loss due to undetected leaks is a significant issue for both consumers and water utilities. Smart meters provide granular consumption data that can be analyzed to detect abnormal patterns. This prototype implements a basic leak detection algorithm inspired by industry practices such as **Minimum Night Flow (MNF)** and **Period Without Null Consumption (PWNC)**.

## Methodology

The detection algorithm is based on a simple rule: a continuous leak is suspected if water usage never drops below a defined threshold over a configurable time window (e.g., 24 hours). This approach mirrors the concept of "continuous flow" detection used by many smart meter systems (e.g., Smartvatten, Aurora Water). The algorithm works as follows:

1. Read hourly water usage data from a CSV file with columns `timestamp` and `usage_liters`.
2. Slide a window of size `N` hours (default 24) across the data.
3. For each window, compute the minimum usage value.
4. If the minimum usage is greater than a threshold (default 0.5 liters per hour), flag that window as a potential leak.

This method is effective for detecting small, constant leaks that cause a baseline consumption even during periods of no activity (e.g., overnight).

## How to Run

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only standard library modules)

### Installation

Clone the repository:

```bash
git clone https://github.com/britdev071809/smart-meter-leak-detector.git
cd smart-meter-leak-detector
```

### Usage

Run the detection script on the included sample data:

```bash
python analyze_usage.py
```

You can customize the detection parameters:

```bash
python analyze_usage.py --threshold 1.0 --window 12 --file your_data.csv
```

- `--threshold`: leak detection threshold in liters per hour (default 0.5)
- `--window`: sliding window size in hours (default 24)
- `--file`: path to the CSV file (default `sample_data.csv`)

### Sample Data

The repository includes `sample_data.csv` with two days of simulated hourly water usage:

- **Day 1 (2025-01-01)**: Normal pattern – usage drops to zero overnight (hours 0–5, 22–23) and is 10 L/h during daytime.
- **Day 2 (2025-01-02)**: Leak pattern – a constant leak of 1.5 L/h persists throughout the entire 24‑hour period.

Running the script on this sample data will output:

```
Potential continuous leak detected from 2025-01-02 00:00:00 to 2025-01-02 23:00:00
```

## Algorithm References

The algorithm draws on established leak‑detection techniques described in the literature and used by water‑monitoring platforms:

- **Minimum Night Flow (MNF)** – the lowest flow observed during nighttime when normal usage is minimal; a sustained elevated MNF indicates a leak (see IEEE paper “Water Consumption Analysis for Real‑Time Leakage Detection”).
- **Period Without Null Consumption (PWNC)** – a duration where flow never falls to zero, signaling a continuous leak (same source).
- **Continuous‑flow thresholds** – many utilities issue leak alerts when usage exceeds a set rate (e.g., 2 gal/hour) for 24 consecutive hours (City of Aurora Water Alerts).
- **Smartvatten’s leak detection** – uses minute‑level monitoring between 00:00‑06:00 and triggers alarms when consumption exceeds a threshold every hour during that window.

## Future Enhancements

This prototype is intentionally simple. Possible extensions include:

- Incorporating machine‑learning models for anomaly detection.
- Adding support for sub‑hourly (e.g., 15‑minute) data.
- Integrating with real‑time data streams from smart meter APIs.
- Providing visualizations of usage patterns and leak alerts.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License – see the LICENSE file for details.