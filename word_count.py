"""
wordCount.py

Counts all distinct words and their frequencies from all text files in the current folder.
Usage:
Just run the program inside the folder containing the data files.
"""

import os
import time

RESULTS_FILE = "WordCountResults.txt"

def read_words_from_file(filename):
    """Reads words from a file and ignores invalid entries."""
    words = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_words = line.strip().split()
                for word in line_words:
                    if word:
                        words.append(word)
    except FileNotFoundError:
        print(f"Error: File not found -> {filename}")
    except IsADirectoryError:
        print(f"Error: Expected a file but got a directory -> {filename}")
    return words

def count_word_frequencies(words):
    """Counts frequency of each word."""
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def process_file(filename, output_file):
    """Process a single file and write results to output_file."""
    words = read_words_from_file(filename)
    if not words:
        print(f"No valid words in {filename}.")
        return

    elapsed_time = time.time() - start_time

    results = [f"File: {filename}"]

    freq = count_word_frequencies(words)
    for word, count in sorted(freq.items()):
        results.append(f"Word: '{word}' -> Frequency: {count}")

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