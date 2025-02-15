import string


def print_rangoli(size):
    L = []
    alpha = string.ascii_lowercase
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))


if __name__ == '__main__':
    print_rangoli(10)
