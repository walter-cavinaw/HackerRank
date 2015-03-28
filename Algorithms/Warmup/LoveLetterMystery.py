alp = "abcdefghijklmnopqrstuvwxyz"
n = int(raw_input())
for i in range(n):
    word = [x for x in raw_input()]
    num = 0
    for i in range(len(word)-1//2):
        while word[i] != word[-i-1]:
            index1 = alp.index(word[i])
            index2 = alp.index(word[-i-1])
            num += 1
            if index1 > index2: word[i] = alp[index1-1]
            else: word[-i-1] = alp[index2-1]
    print num
