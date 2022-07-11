def split(word):
    return [char for char in word]
     
n=int(input())
for i in range(0,n):
    m=input()
    heh=split(m)
    lst=[]
    heh.append('0')
    count=0
    for h in heh:
        if h not in lst:
            if len(lst)==3:
                count=count+1
                lst.clear()
            lst.append(h)
        if h=='0':
            if len(lst)>1:
                count=count+1
    print(count)