def rse(v):
    contagem  = {}
    for i, x  in enumerate(v):
        if x in contagem.keys():
            contagem[x] += 1
        else:
            contagem[x] = 1
            
    for i, x in enumerate(v):
        if contagem[x] == 1:
            return x
    
    return None


if __name__== "__main__":
    v = [5,3,5,1,3,4,7,7,4,3]
    print(rse(v))