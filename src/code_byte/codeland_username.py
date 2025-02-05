# # Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine 
# if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.


import re, string
def CodelandUsernameValidation(strParam):
    username = strParam
    username_letters = [ letter for letter in strParam]
    responses = 0
    un_match = f'^([_a-zA-Z0-9]*)[a-zA-Z0-9]+$'

    if len(username) >= 4 and len(username) <= 25: 
        responses += 1
    if username_letters[0].isalpha():
        responses += 1
    if bool(re.match(un_match, username)):
        responses += 1
    
    return responses == 3


# keep this function call here 
print(CodelandUsernameValidation(input()))