# File Name: reconstructSentence.py
# This program functions to read two text files and combine their contents to
# create a complete output.
# This program takes the names of the text files as command line arguments
# Example Invocation: python3 reconstructSentence.py input1.txt input2.tx
 

import sys

with open(sys.argv[1], 'r') as file1:
  list1 = file1.read().strip().split()

with open(sys.argv[2], 'r') as file2:
  list2 = file2.read().strip().split()

out = []

len1 = len(list1)
len2 = len(list2)
while len1 > 0 or len2 > 0:
  if len1 > 0:
    out.append(list1[len1 - 1])
    del list1[len1 - 1]
    len1 -= 1
  if len2 > 0:
    out.append(list2[len2-1])
    del list2[len2 - 1]
    len2 -= 1

with open("output.txt", "w") as output_file:
  for word in out:
    output_file.write(word + " ")

print(out)
