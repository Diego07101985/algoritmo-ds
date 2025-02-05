# First Reverse
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: 
# if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH


# Input: "I Love Code"
# Output: edoC evoL I

def FirstReverse(strParam):
  word_param = ""
  size_frase = len(strParam)-1
  for i in range(size_frase,-1,-1):  
      word_param += strParam[i]

  return word_param

# # keep this function call here 
print(FirstReverse("coderbyte"))