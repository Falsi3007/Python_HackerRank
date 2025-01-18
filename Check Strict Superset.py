# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
n=int(input())
count=0
for i in range(n):
    s=set(map(int,input().split()))
    if(s-a==set() and len(s)<len(a)):
        count+=1
if count==n:
    print("True")
else:
    print('False')
