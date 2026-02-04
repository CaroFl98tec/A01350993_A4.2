"""
computeStatistics.py

Automatically computes descriptive statistics from all numeric files in the current folder.
Statistics calculated:
- Mean
- Median
- Mode
- Variance
- Standard Deviation

Usage:
Just run the program inside the folder containing the data files.
"""

import os
import time
import math

RESULTS_FILE = "StatisticsResults.txt"


def read_numbers_from_file(filename):
    """Reads numeric values from a file and ignores invalid entries."""
    numbers = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                value = line.strip()
                try:
                    number = float(value)
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid data ignored: {value} in {filename}")
    except FileNotFoundError:
        print(f"Error: File not found -> {filename}")
    except IsADirectoryError:
        print(f"Error: Expected a file but got a directory -> {filename}")
    return numbers


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    middle = count // 2
    if count % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    return sorted_numbers[middle]


def calculate_mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_freq = max(frequency.values())
    mode_values = [num for num, freq in frequency.items() if freq == max_freq]
    return mode_values[0]


def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def calculate_standard_deviation(variance):
    return math.sqrt(variance)


def process_file(filename, output_file):
    """Process a single file and write results to output_file."""
    numbers = read_numbers_from_file(filename)
    if not numbers:
        print(f"No valid numeric data in {filename}.")
        return

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_standard_deviation(variance)

    elapsed_time = time.time() - start_time

    results = [
        f"File: {filename}",
        f"Mean: {mean}",
        f"Median: {median}",
        f"Mode: {mode}",
        f"Variance: {variance}",
        f"Standard Deviation: {std_dev}",
        f"Execution Time (seconds): {elapsed_time}",
        "-" * 40
    ]

    for line in results:
        print(line)
        output_file.write(line + "\n")


if __name__ == "__main__":
    start_time = time.time()

    # List all .txt files in the current folder
    files_to_process = sorted([f for f in os.listdir('.') if f.lower().endswith('.txt')])

    if not files_to_process:
        print("No .txt files found in the current folder.")
        exit(1)

    # Open the results file once and process all files
    with open(RESULTS_FILE, "w", encoding="utf-8") as out_file:
        for file_name in files_to_process:
            process_file(file_name, out_file)

    print(f"\nAll results saved in '{RESULTS_FILE}'.")