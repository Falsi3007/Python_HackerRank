t = int(input())

for _ in range(t):
    _=input()
    a = set(map(int, input().split()))
    _=input()
    b = set(map(int, input().split()))
    
    print(a.issubset(b))
