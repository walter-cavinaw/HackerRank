def lonelyinteger(a):
    items = []
    for x in a:
        if x not in items:
            items.append(x)
        else:
            items.remove(x)
    return items[0]
        

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
