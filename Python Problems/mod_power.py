def pow(a,b):
    if b==1:
        return a
    elif b%2==0:
        return pow(a*a,b//2)
    else:
        return a*pow(a*a,b//2)

a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b)%m)

