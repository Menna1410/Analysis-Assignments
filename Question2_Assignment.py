

import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    sorted_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            sorted_arr.append(left_half[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right_half[right_idx])
            right_idx += 1

    sorted_arr.extend(left_half[left_idx:])
    sorted_arr.extend(right_half[right_idx:])
    return sorted_arr

def find_pairs_with_sum(S, target):
    pairs = set()  
    sorted_S = merge_sort(S)
    
    for num in sorted_S:
        complement = target - num
        if binary_search(sorted_S, complement) and complement != num:
            pairs.add((num, complement))
    return list(pairs)

n_values = list(range(1, 10001, 100))
execution_times = []
target = 15

for n in n_values:
    S = [random.randint(1, 1000) for _ in range(n)]

    start_time = time.time()
    find_pairs_with_sum(S, target)
    end_time = time.time()

    execution_time = end_time - start_time
    execution_times.append(execution_time)

plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, label='Execution Time', marker='o')
plt.xlabel('List Size (n)')
plt.ylabel('Execution Time (s)')
plt.grid(True)
plt.title('Algorithm Scalability')
plt.show()