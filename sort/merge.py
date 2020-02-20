from typing import List


def merge_sort_recursive(nums, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort_recursive(nums, left, mid)
        merge_sort_recursive(nums, mid + 1, right)
        merge_recursive_helper(nums, left, mid, right)


def merge_recursive_helper(nums, left, mid, right):
    left_length = mid - left + 1
    right_length = right - mid
    left_end = True
    L = nums[left : mid + 1]
    R = nums[mid + 1 : right + 1]
    l = r = 0
    k = left
    while l < left_length and r < right_length:
        if L[l] <= R[r]:
            nums[k] = L[l]
            l += 1
        else:
            nums[k] = R[r]
            r += 1
        k += 1
    if l >= left_length:
        nums[k : right + 1] = R[r:]
    else:
        nums[k : right + 1] = L[l:]

def merge_sort_iterative(nums):
    pass

if __name__ == "__main__":
    a = [5, 2, 4, 7, 1, 3, 2, 6]
    merge_sort_recursive(a, 0, len(a) - 1)
    print(a)
