fb=1
sum=0
prev=0
while True:
    x=prev
    prev=fb
    fb=prev+x
 #   print fb
    if fb > 4000000:
        print "last fb is", fb
        break
    if fb%2==0:
        sum=sum+fb


print "the sum is ",sum
