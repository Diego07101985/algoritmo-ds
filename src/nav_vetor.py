def big_num(v, n ):
    soma = sum(v[:n])
    
    for i in range(n-1,-1,-1):
        new_sum = sum(v[:i]) + sum(v[(i-n):]) 
        soma = max(soma,new_sum)
    return  soma


if __name__== "__main__":
    v = [8,7,8,9,1,2,1,4]
    v1 = [5,0,-1,3,-2,5,7,9]
    v2 = [7,1,3,-1,3,0,7,1]
    print(big_num(v2, 5))