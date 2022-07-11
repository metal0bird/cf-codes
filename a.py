n=int(input())
for i in range(0,n):
    m=input()
    if int(m)==1:
        print(0)
    elif int(m)<10:
        print(int(m)-1)
    else:
        if m[0]=='1':
            print(m[1:])
        else:
            print(int(m[0])-1,end="")
            print(m[1:])
