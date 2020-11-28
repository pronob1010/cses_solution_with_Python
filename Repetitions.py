s = input()
A = 0
T = 0
C = 0
G = 0

tA = 0
tT = 0
tC = 0
tG = 0
for i in range(len(s)):
    if s[i]=='A':
        tT = 0
        tC = 0
        tG = 0
        if A<=tA:
            A = tA
        tA += 1

    elif s[i]=='T':
        tA = 0
        tC = 0
        tG = 0
        if T<=tT:
            T = tT
        tT += 1
    elif s[i]=='C':
        tA = 0
        tT = 0
        tG = 0
        if C <= tC:
            C = tC
        tC += 1
    elif s[i] == 'G':
        tA = 0
        tT = 0
        tC = 0

        if G <= tG :
            G = tG
        tG += 1

print(max(A,T, G, C)+1)

