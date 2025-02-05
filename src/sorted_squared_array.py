def sortedSquaredArray(array):
    array  = [value * value for value in array]
    for i in reversed(range(len(array))):
        for j in reversed(range(len(array))):
            if abs(array[i]) > abs(array[j]):
                tmp_value = array[j]
                array[j] = array[i] 
                array[i] = tmp_value                                                 

    return array

def merge_sort(array):
    
    if len(array) <= 1:
        return array

    median_point = len(array)//2
    
    left_half = array[0:median_point]
    right_half = array[median_point:len(array)-1]
    
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array  = []
    i= j = 0
    
    while i < (len(left)-1) and j < (len(right)-1):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

                                
    

if __name__== "__main__":
    array  =  [5,2,3,1]
    print(merge_sort(array))
    #print(sortedSquaredArray(array))

