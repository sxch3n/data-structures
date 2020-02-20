from typing import List


def quick_sort(nums: List[int], low, high):
    if low < high:
        pivot_idx = partition(nums, low, high)
        quick_sort(nums, low, pivot_idx - 1)
        quick_sort(nums, pivot_idx + 1, high)


def partition(nums: List[int], low, high):
    pivot = nums[low]

    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low], nums[high] = nums[high], nums[low]
        while low < high and nums[low] <= pivot:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]

    return low


"""optimize"""


def qucik_sort_optimized(nums, low, high):
    """
    Use iteration to reduce recurtion stack.
    """
    while low < high:
        pivot_idx = partition_optimized(nums, low, high)
        quick_sort(nums, low, pivot_idx - 1)
        low = pivot_idx + 1


def partition_optimized(nums, low, high):
    """
    Reduce unecessary element movement through the process
    """
    pivot = nums[low]   # If optimize the pivot selection, 
    startIdx = low      # the start index should be changed too.
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        while low < high and nums[low] <= pivot:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]
    nums[startIdx], nums[low] = nums[low], nums[startIdx]
    return low

def select_pivot(nums):
    '''
    randomly choose pivot. (lengh >= 9)
    randomly choose 9 elements from the array, divide into 3 groups of 3 elements each.
    randomly choose 1 element from each group.
    randomly choose the only one from the 3 elements.
    '''
    pass

if __name__ == "__main__":
    count = 0
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(a, 0, len(a) - 1)
    print(a)
    b = [2, 8, 7, 1, 3, 5, 6, 4]
    qucik_sort_optimized(b, 0, len(b) - 1)
    print(b)
