
#Find Intersection
# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
# the first element will represent a list of comma-separated numbers sorted in ascending order,
# the second element will represent a second list of comma-separated numbers (also sorted).
# Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection,
# return the string false.

# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1,4,13

def FindIntersection(strArr):
  output = []
  number_elements = 0

  for number in strArr[0].split(','):
      for number2 in strArr[1].split(','):
          if number2 in number:
              if number2 not in output:
                  output.append(f'{number}'.strip())
                  number_elements += 1

  if number_elements < 1:
      return 'false'

  # code goes here
  return ','.join(output)