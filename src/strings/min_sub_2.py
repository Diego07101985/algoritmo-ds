
import numpy as np

def min_sub(N,K):
    sub_str_dic = {}
    keys = [letter for letter  in K]
    group = ""
    for i  in range(len(N)):
        if i < len(N)-(len(K)-1):
            group = N[i:i+len(K)]
            for key in keys:
                if key in group:
                    if key in sub_str_dic.keys():
                        sub_str_dic[key] += 1
                    else:
                        sub_str_dic[key] = 1
            print(sub_str_dic)   
            if sub_str_dic.keys() == len(keys) and len(set(sub_str_dic.values())) == 1:
                return group

            sub_str_dic = {}

if __name__== "__main__":
    N = "aaabaaddae"
    K = "aed"
    print(min_sub(N,K))
    N = "aabdccdbcacd"
    K = "aad"
    print(min_sub(N,K))