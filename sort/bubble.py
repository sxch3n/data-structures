from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 2):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble_sort_with_flag(nums: List[int]) -> List[int]:
    """
    Stop when flag is True, which indicates the list has 
    no change since last iteration.
    """
    for i in range(len(nums) - 1):
        flag = True
        for j in range(len(nums) - 2):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
        if flag:
            break
    return nums


def bubble_sort_with_flag_and_last_pos_pointer(nums: List[int]) -> List[int]:
    """
    recorded last position the swap happened and the end of the unsorted array.
    """
    lastPos = 0
    sortEnd = len(nums) - 1
    for i in range(len(nums) - 1):
        flag = True
        j = 0
        while j < sortEnd:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
                lastPos = j
            j += 1
        if flag:
            break
        sortEnd = j
    return nums


if __name__ == "__main__":
    a = [5, 4, 3, 2, 1, 7, 8, 6, 9]
    print(bubble_sort_with_flag_and_last_pos_pointer(a))
