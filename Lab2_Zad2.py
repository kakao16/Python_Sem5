
import multiprocessing

import random

def merge(left, right):
    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left

    result = []
    i_left = i_right = 0

    while len(result) < len(left) + len(right):
        if left[i_left] >= right[i_right]:
            result.append(right[i_right])
            i_right += 1
        else:
            result.append(left[i_left])
            i_left += 1

        if i_right == len(right):
            result += left[i_left:]
            break
        
        if i_left == len(left):
            result += right[i_right:]
            break

    return result

def merge_sort(arr):
    N = len(arr)
    
    if N < 2:
        return arr

    middle = N // 2
    
    return merge(left = merge_sort(arr[:middle]), right = merge_sort(arr[middle:]))


def parallel_merge_sort(arr, num_processes=None):
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)

    sorted_arr = []
    for chunk in sorted_chunks:
        sorted_arr = merge(sorted_arr, chunk)
    
    return sorted_arr


if __name__ == "__main__":
    test_array = [random.randint(0, 1000) for _ in range(1000)]

    print("Input: ")
    print(test_array)

    output_array = parallel_merge_sort(test_array)
    print("Output: ")
    print(output_array)

