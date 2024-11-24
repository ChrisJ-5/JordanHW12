# File Name: sumLines.py
# This script functions to read integers from a text file into a list and
# calculate the sum, the number of integers, and the average.
# This program takes the name of the text file as a command line argument.
# Example Invocation: python3 sumlines.py dataInput.txt

import sys

total_sum = 0
total_count = 0

def process_line(line):
  global total_sum
  global total_count
  if line.strip():
    numbers = line.split()

    for num_str in numbers:
      num = int(num_str)
      total_sum += num
      total_count += 1

with open(sys.argv[1], 'r') as file:
  for line in file:
    process_line(line)

average = total_sum / total_count

print(total_sum, total_count, average)


