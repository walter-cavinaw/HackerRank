n = int(raw_input())
for i in range(n):
    word = raw_input()
    rem = 0
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            rem +=1
    print rem
