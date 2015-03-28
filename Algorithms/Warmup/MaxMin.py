n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
min_diff = candies[-1]
for x in xrange(n-k+1):
    newmin = candies[x+k-1] - candies[x]
    min_diff = newmin if newmin<min_diff else min_diff

print min_diff
