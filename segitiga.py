def segitiga(inputan):
    mid = inputan//2
    mid1 = mid
    mid2 = mid
    for i in range(mid+1):
        for j in range(inputan):
            if i==0:
                if j==mid:
                    print("*",end='')
                else:
                    print(" ",end='')
            elif i>0 and i<mid:
                if j==mid1 or j==mid2:
                    print("*",end='')
                elif j>mid1 and j<mid2:
                    print("*",end='')
                else:
                    print(" ",end='')
            elif i==mid:
                print("*",end='')
        print("")
        mid1-=1
        mid2+=1

def segitigaBackWard(inputan):
    mid = inputan//2
    inCol = -1
    lastCol = inputan
    

    for i in range(mid+1):
        for j in range(inputan):
            if i==0:
                print("*",end='')
            elif i>0 and i<mid:
                if j==inCol or j==lastCol:
                    print(" ",end='')
                elif j<inCol or j>lastCol:
                    print(" ",end='')
                else:
                    print("*",end='')
            elif i==mid:
                if j==mid:
                    print("*",end='')
                else:
                    print(" ",end='') 
        print("")
        inCol+=1
        lastCol-=1
        

while 1:
    segitigaBackWard(23)
    segitiga(23)
