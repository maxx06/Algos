#Binary Search
#May 2021

def binarySearch(array, target) -> int:
    array.sort()
    print(array)
    left, right = min(array), max(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] >= target:
            right = mid
        else:
            left = mid + 1
    print(left)
    return left