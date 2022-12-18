# How to run
# py mergesort_cpu.py matrix_size

# Example
# py mergesort_cpu.py 1000000

import numpy as np
import time
import sys


def merge_sort(items):
    if len(items) <= 1:
        return items

    # Split the list into two halves
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves and return the result
    return merge(left, right)

# ngegabungin 2 list


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Merge the lists until one is empty
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining items from the non-empty list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Get matrix size from terminal argument
matrix_size = int(sys.argv[1])

np.random.seed(0)
items = np.random.randint(size=matrix_size, low=0, high=100)

# Start time
start = time.time()

sorted_items = merge_sort(items)

# End time
end = time.time()

print("Time: ", end - start)
