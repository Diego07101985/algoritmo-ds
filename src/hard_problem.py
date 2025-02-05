
def mediana(v1, v2 ):
    mediana_v1 =(v1[(round((len(v1)/2))-1)] +  v1[round((len(v1)/2))])/2 if len(v1) % 2 == 0 else v1[round(len(v1)/2)+1]
    mediana_v2 = (v2[(round((len(v2)/2))-1)] +  v2[round((len(v2)/2))])/2 if len(v2) % 2 == 0 else v2[round(len(v2)/2)+1]


    return (mediana_v1 + mediana_v2) / 2


if __name__== "__main__":
    v = [1,3,7,9]
    v1 = [1,5,9,20]
    print(mediana(v, v1))