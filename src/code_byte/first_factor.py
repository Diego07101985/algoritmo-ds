
# Discussion Solutions 
# First Factorial
# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. 
# For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
# For the test cases, the range will be between 1 and 18 and the input will always be an integer.
# Input: 8
# Output: 40320

def FirstFactorial(num):
  
  factor = 1
  for i in range(num,0,-1):
      factor = factor * i

  # code goes here
  return factor

# keep this function call here 
print(FirstFactorial(8))