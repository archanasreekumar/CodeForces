n,m,a=raw_input().split(" ")
n=int(n)
m=int(m)
a=int(a)
num = 0

if n%a==0 and m%a==0:
    num = (n/a)*(m/a)

if n%a==0 and m%a!=0:
    num = ((n/a)*(m/a))+(n/a)

if m%a==0 and n%a!=0:
    num = ((m/a)*(n/a))+(m/a)
    
if m%a!=0 and n%a!=0:
     num = ((m/a)*(n/a))+(m/a)+(n/a)+1
    

    
print num