t = int(input())
s = list(map(int, input().split()))


c = 0
p = 0
for i in range(1,len(s)-1):
    # print(s[i-1], s[i], s[i+1])
    if s[i-1]<= s[i] <= s[i+1]:
        c+=1

x = len(s)-c

print(x)
# 3 2 5 1 7
# 2 3 5 1 7
# 2 3 1 5 7
# 2 1 3 5 7
# 1 2 3 5 7
#
#
# 2 1 5
# 1 2 5
#
# 1 + 2+ 3
#
# 1 8 5 4 5 6
# 1 5 8 4 5 6
# 1 5 4 8 5 6
# 1 4 5 8 5 6
# 1 4 5 5 8 6
# 1 4 5 5 6 8
# 6666666666666
#

