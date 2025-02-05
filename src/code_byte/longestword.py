import string

def LongestWord(sen):
   lenght_word = []
   term = sen.translate(str.maketrans('', '', string.punctuation))
   words = term.split(" ")
   for word in words:
       lenght_word.append(len(word))
   index = lenght_word.index(max(lenght_word))
   return words[index]


# keep this function call here 
print(LongestWord(input()))