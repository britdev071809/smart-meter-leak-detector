import csv
import argparse
from datetime import datetime


def load_data(filepath):
    """Load timestamp and usage data from CSV."""
    data = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamp = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
            usage = float(row['usage_liters'])
            data.append((timestamp, usage))
    return data


def detect_leak(data, threshold, window_size):
    """
    Detect continuous leaks where usage stays above threshold for the whole window.
    Returns a list of (start, end) datetime pairs.
    """
    leaks = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        usages = [usage for _, usage in window]
        if min(usages) > threshold:
            leaks.append((window[0][0], window[-1][0]))
    return leaks


def main():
    parser = argparse.ArgumentParser(
        description='Detect continuous leaks in smart meter data.'
    )
    parser.add_argument('--file', default='sample_data.csv',
                        help='Path to CSV file (default: sample_data.csv)')
    parser.add_argument('--threshold', type=float, default=0.5,
                        help='Threshold for leak detection (liters per hour, default: 0.5)')
    parser.add_argument('--window', type=int, default=24,
                        help='Window size in hours (default: 24)')
    args = parser.parse_args()

    data = load_data(args.file)
    leaks = detect_leak(data, args.threshold, args.window)

    if leaks:
        for start, end in leaks:
            print(f'Potential continuous leak detected from {start} to {end}')
    else:
        print('No continuous leak detected.')


if __name__ == '__main__':
    main()