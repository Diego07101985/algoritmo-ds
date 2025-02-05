
# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    # Write your code here
    return binaryHelper(array, target, 0 , len(array)-1)

    

def binaryHelper(array, target, left , right):
    
    if left > right:
        return -1
        
    mid_index = (left + right)//2

    if target == array[mid_index]:
        return mid_index
    elif target < array[mid_index]:
        return binaryHelper(array, target, left, mid_index-1)
    else:
        return binaryHelper(array, target, mid_index+1, right)
    
    
    
def binaryHelper(array, target, left , right):
    
    while left <= right:
        mid_index = (left + right)//2

        if target == array[mid_index]:
            return mid_index
        elif target < array[mid_index]:
            right =  mid_index -1 
        else:
            left = mid_index +1
            
    return -1