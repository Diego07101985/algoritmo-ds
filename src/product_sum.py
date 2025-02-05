# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier  = 1):
    # Write your code here.
    result = 0
    for element in array:
        if type(element) is list:
            result += productSum(element, multiplier +1)
        else:
            result += element            
    
    return result * multiplier