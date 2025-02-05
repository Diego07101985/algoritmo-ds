text = "EEDDEDEEEDDDEEDD"


def contar(text):
    stack = []
    count_substring = 0
    tmp_letter = text[0]

    for letter in text:

        if letter == tmp_letter:
            stack.append(letter)
        else:
            if len(stack) ==0:
                tmp_letter = letter
                stack.append(letter)
            else:
                stack.pop()
                if len(stack) ==0:
                    count_substring += 1
    
    return count_substring

if __name__=="__main__":
    print(contar("EEDDEDEEEDDDEEDD"))
    print(contar("EDDDDEEEDE"))
    