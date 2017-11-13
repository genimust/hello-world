annee = input ("saisir l'annee a verifier")

if annee%4 !=0 :
    print "l'annee", annee, " n'est pas bissextile"
elif annee%100 ==0 :
    if annee%400 ==0:
        print "l'annee", annee, " est  bissextile"
    else :
        print ("l'annee", annee, " n'est pas bissextile")
else:
    print ("l'annee", annee, " n'est pas bissextile")


