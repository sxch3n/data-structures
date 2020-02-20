from typing import List

def insertion_sort(nums: List[int]):
    
    
    for i in range(1,len(nums)):        
        num = nums[i]
        for j in range(i-1,-1,-1):
            if nums[j]>= num:
                nums[j], nums[j+1] = nums[j+1],nums[j]
            else:
                nums[j] = num
                break
    
    return nums


if __name__ == '__main__':
    a = [5,4,3,2,1]
    print(insertion_sort(a))