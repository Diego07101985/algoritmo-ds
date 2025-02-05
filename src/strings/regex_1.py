
import re
email  = "Este é o meu currículo. Meu email é cleuton.sampaio@teste.com.br ou então pode usar o cleuton@codechallenge.com, pois respondo em ambos (emails falsos!)"

emails = re.findall('\\b[\\w+]*[.]?[\\w+]+@[\\w+]+.\\w+.\\w*\\b',email )
print(emails)