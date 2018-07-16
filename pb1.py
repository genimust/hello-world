i=1
j=1
k=1
st=0
sf=0
sd=0
a=0
b=0
c=0
print "start"
while True:
    a=i*3
    st=st+a
    print a
    i=i+1
    if i*3 >=1000:
        break


print "st = ",st

while True:
    b=j*5
    sf=sf+b
    print b
    j=j+1
    if j*5 >=1000:
        break

print "sf = ",sf

while True:
    c=k*15
    sd=sd+c
    print c
    k=k+1
    if k*15 >=1000:
        break

print "sd = ",sd


print "solution is",st+sf-sd

