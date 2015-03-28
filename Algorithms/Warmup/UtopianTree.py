def growth(c):
    if c == 0:
        return 1
    if c % 2 == 1:
        return 2*growth(c-1)
    else:
        return growth(c-1)+1

if __name__ == '__main__':
    n = int(raw_input())
    for x in range(n):
        i = int(raw_input())
        print growth(i)
