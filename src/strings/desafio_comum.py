romano_arabico = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}


numero_romano = "MCMXIX"
arabic_value = 0
i=0

while i < len(numero_romano):
    c = numero_romano[i]
    v1 = romano_arabico[c]
    if i < (len(numero_romano)-1):
        v2 = romano_arabico[numero_romano[i+1]]
        if v1<v2:
            v1*=-1
            arabic_value +=v2
            i+=1
        arabic_value +=v1
        i=i+1

print(arabic_value)