#for i in "00456":
#   print i
import gc
i=1L
j=1
print "start"
for i in range( 1, 999999999):
    j=1
    while j<=11:
        if j==11:
            print "bingo",i
            exit()
        if (i % j !=0):
           break
        gc.collect()
        j=j+1



