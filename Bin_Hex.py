"""
convertNumbers.py

Automatically converts numeric values from all files in the current folder to binary and hexadecimal.
Usage:
Just run the program inside the folder containing the data files.
"""

import os
import time

RESULTS_FILE = "ConvertionResults.txt"

def read_numbers_from_file(filename):
    """Reads numeric values from a file and ignores invalid entries."""
    numbers = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                value = line.strip()
                try:
                    number = int(value)
                    numbers.append(number)
                except ValueError:
                    print(f"Invalid data ignored: {value} in {filename}")
    except FileNotFoundError:
        print(f"Error: File not found -> {filename}")
    except IsADirectoryError:
        print(f"Error: Expected a file but got a directory -> {filename}")
    return numbers

def convert_to_binary(number):
    """Converts a number to binary using basic algorithm."""
    if number == 0:
        return "0"
    binary = ""
    n = number
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def convert_to_hex(number):
    """Converts a number to hexadecimal using basic algorithm."""
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    n = number
    while n > 0:
        hex_str = hex_chars[n % 16] + hex_str
        n = n // 16
    return hex_str

def process_file(filename, output_file):
    """Process a single file and write results to output_file."""
    numbers = read_numbers_from_file(filename)
    if not numbers:
        print(f"No valid numeric data in {filename}.")
        return

    elapsed_time = time.time() - start_time

    results = [f"File: {filename}"]

    for number in numbers:
        binary = convert_to_binary(number)
        hexa = convert_to_hex(number)
        results.append(f"Number: {number} -> Binary: {binary}, Hexadecimal: {hexa}")

    results.append(f"Execution Time (seconds): {elapsed_time}")
    results.append("-" * 40)

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