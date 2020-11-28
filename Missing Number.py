n = int(input())
s = list(map(int, input().split()))
x = sum(s)
y = 0
for i in range(1,n+1):
    y+=i
print(y-x)