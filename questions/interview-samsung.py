#
# Find the element that appears once in a sorted array
# Given a sorted array in which all elements appear twice (one after one) 
# and one element appears only once. Find that element 
# in O(log n) complexity.

# Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}
# Output:  4
# Input:   arr[] = {1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8}
# Output:  8

'''
tag : Binary Search 
Because the array is sorted and duplicated elements appears twice,
then the index of the element before the single element 
has pattern arr[k]==arr[k+1] where k is even (belongs to (0,2,4...)),
which equals arr[p] == arr[p-1] where p is odd (belongs to (1,3,5..)),
otherwise, it apears opposite.
So each time check the middle index and the element,
If the middle index is odd and 
if the middle element equals to the left, do the search on the right part.
else do BS on the left part.
If the middle index is even and 
if the element equals to the right, do the search on the right part,
else do BS on the left part.
'''
def BS(arr,left,right):
  
  # if the left is beyond the right, then the array is full of pairs
  if left > right:
    return None
  
  # if the left is equal to the right, that's the element we want
  if left == right:
    return arr[left]
  
  # calculate the middle index
  mid = left + (right - left)//2
  
  # check if the middle index is even or not
  if mid %2==0:
    # decide which part to do BS next
    # matches the right, do BS on right
    if arr[mid] == arr[mid+1]:
      # start from [the next right to the right]  to end- mid+2
      return BS(arr,mid+2,right)       
    # matches the left, do BS on left
    if arr[mid] == arr[mid-1]:
      # start from left to [the next left to the left]  to end- mid+2
      return BS(arr,left,mid-2)
  else: # when the middle index is odd
    # mathces the left, do BS on right
    if arr[mid] == arr[mid-1]:
      
      return BS(arr,mid+1,right)    
    # matches the right, do BS on left
    if arr[mid] == arr[mid+1]:
      return BS(arr,left,mid-1)
      

  
# give the initial left and right as the start and the end of the array.
print(BS(arr,0,len(arr)-1))