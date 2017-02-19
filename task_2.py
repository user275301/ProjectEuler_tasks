a=1
b=1
res=0

while a<4000000:
    (a,b)=(a+b,a)
    if a%2==0:
        res+=a

print(res)
