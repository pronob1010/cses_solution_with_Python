n = int(input())
while True:
    if n == 1:
        print(1)
        break
    elif n%2==0:
        print(n, end=" ")
        n = n//2
    else:
        print(n, end=" ")
        n = ((n*3)+1)