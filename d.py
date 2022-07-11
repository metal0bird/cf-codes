def split(word):
    return [char for char in word]
     

#n=int(input())
n=1
for i in range(0,n):
    st=input()
    k=int(input())
    st=split(st)
    sum=0
    for j in st:
        sum=sum+(ord(j)-96)
    while(sum>k):
        sum=sum-(ord(max(st))-96)
        print(max(st))
        st.remove(max(st))
    print(st)