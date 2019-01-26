import time
b = 6

while b!=0 :
    i=1
    print ("table de multiplication de ", b)
    while i <10 :
        print (b, "*", i,"=", b*i)
        time.sleep(2)
        i +=1
    b = b- 1
