def split(word):
    return [char for char in word]
     

#n=int(input())
n=1
for i in range(0,n):
    st=input()
    st=split(st)
    lst=[]
    st.append('0')
    st.append('1')
    count=0
    for j in st:
        print(j)
        if j=='1':
            if len(list[lst])>1:
                print("lmao")
                count=count+1
        if j in lst:
            print("continue")
            continue
        else:
            lst.append(j)
            print(lst)
        if len(lst)==4:
                count=count+1
                print("clear")
                lst=list[lst[-1]]
    print(count)
