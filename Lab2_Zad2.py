
import multiprocessing

import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

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
    arr_sizes = [500, 5000, 100000, 500000]
    time_parallel = []
    time_single = []

    for i in arr_sizes:
        test_array = [random.randint(0, 999999) for _ in range(i)]
        
        start = timer()
        output_array1 = parallel_merge_sort(test_array)
        end = timer()
        time_parallel.append(end-start)

        start = timer()
        output_array2 = merge_sort(test_array)
        end = timer()
        time_single.append(end-start)
        
    plt.plot(arr_sizes, time_parallel)
    plt.plot(arr_sizes, time_single)
    
    plt.title("Time taken to sort")
    plt.ylabel("Time [s]")
    plt.xlabel("Number of elements")
    plt.legend(["Parallel", "Single thread"])
    plt.show()
    
    

    


