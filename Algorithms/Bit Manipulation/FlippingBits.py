if __name__ == '__main__':
    n = int(raw_input())
    for x in range(n):
        i = int(raw_input())
        i = i^int('0xffffffff',16)
        print i
