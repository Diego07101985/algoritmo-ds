def rse(v):
    for i, x  in enumerate(v):
        mk = False
        for j, y in enumerate(v):
            if i!=j and x==y:
                mk = True
                break
    
        if not mk:
            return x
    
    return None


if __name__== "__main__":
    v = [5,3,5,1,3,4,7,7,4,3]
    print(rse(v))