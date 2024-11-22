# Stanisław Kusiak

import random

def bubble_sort(arr):
    N = len(arr)
    
    for i in range(N):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr


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

    return merge( left = merge_sort(arr[:middle]), right = merge_sort(arr[middle:]) )


test_array = [random.randint(0, 1000) for _ in range(10)]

print("Input: ")
print(test_array)

output_array = merge_sort(test_array)
print("Output: ")
print(output_array)
