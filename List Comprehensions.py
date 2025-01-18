if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n ]               
    print(list1)



#in another method
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list1=[] 
    for i in range(0,x+1):
        for j in range (0, y+1):
            for k in range(0,z+1):
                if (i+j+k != n):
                    list1.append([i, j, k])        
    print(list1)
