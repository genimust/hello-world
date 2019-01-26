#for i in "00456":
#   print i
import gc

i=1
j=1
print "start"
for i in range( 232792550, 232792570):
    j=1
    while j<=21:
        if j==21:
            print "bingo",i
            exit()
        print i,j
        if (i % j !=0):
           print "ici", "i est ",i , "j est ", j ,"mod ",i%j
           break
        j=j+1



