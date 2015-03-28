def  maxXor( l,  r):
    maxi = 0
    for x in range(l, r+1):
        for y in range(l, r+1):
            if maxi<(x^y):
                maxi = x^y
    return maxi

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
