def findMedian(arr):
    # Sort the list in ascending order
    arr.sort()
    
    # Find the middle index
    middle_index = len(arr) // 2
    
    # The middle element is the median
    median = arr[middle_index]
    
    return median