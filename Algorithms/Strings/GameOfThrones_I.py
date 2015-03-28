string = raw_input()
 
found = False
check = []
for x in string:
    if x not in check:
        check.append(x)
    else:
        check.remove(x)
found = (len(check)<=1)
if not found:
    print("NO")
else:
    print("YES")
