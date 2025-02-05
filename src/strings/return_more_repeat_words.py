import string
import nltk
nltk.download('stopwords')


def freq(cancao_exilio):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    remove_stop_words_cancao  = [word for word in cancao_exilio.split(' ') if word not in  stopwords]
    words_cancao_exilio = [word for word in remove_stop_words_cancao if word not in string.punctuation ]
    cancao_exilio_map_words = {}

    for word in words_cancao_exilio:
        if word not in cancao_exilio_map_words.keys():
            cancao_exilio_map_words[word] = 1
        else:
            cancao_exilio_map_words[word] += 1

    max_repeat_word = max(cancao_exilio_map_words.values())
    print([key for key, value in cancao_exilio_map_words.items() if value == max_repeat_word])

if __name__== "__main__":
    cancao_exilio = ""
    with open('src/strings/cancao_exilio.txt', 'r') as file:
        cancao_exilio = file.read()

    cancao_exilio = cancao_exilio.replace('\n', ' ').replace('–', '')
    freq(cancao_exilio)