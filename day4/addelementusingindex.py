n=int(input("enter size"))
a=list(map(int,input().split(' ')))[n:]
sum=0
for i in a:
    sum=sum+i
print(sum)

