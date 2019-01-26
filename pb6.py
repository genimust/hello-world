prenom = " Paul "
nom = " Dupont "
age = 21
print (" Je m'appelle {} {} et j'ai {} ans .".format(prenom, nom , age))


print ("Je m' appelle {0} {1} ({3} {0} pour l' administration ) et j'ai {2}  ans .".format(prenom , nom , age , nom.upper()))

for i in prenom:
    print(i)
chaine="hello World"
try:
    i = 0 # On appelle l'indice 'i' par convention
    while True:
      print(chaine[i])
      i += 1
except IndexError:
    print("ERROR indexation !!!")

ma_liste1 = [3,4,5]
print(ma_liste1)
ma_liste1.insert(2,8)
print(ma_liste1)
ma_liste1.append(44)
print("after append liste2")
print(ma_liste1)
ma_liste2=[11,12,13]
ma_liste1.extend(ma_liste2)
print("maListe1 is ", ma_liste1)

print("######### it time to delete ############")
del ma_liste1[1]
print(ma_liste1)
print("######### it time to remove ############")
ma_liste1.remove(44)
print(ma_liste1)

for i,elt in enumerate(ma_liste1):
 print("a l' indice {} se trouve {}.".format(i,elt))

autre_liste=[["must","hello"],["lll","world"]]
for i in (autre_liste):
    print(i)


def decomposer (entier , divise_par ):
  p_e = entier // divise_par
  reste = entier % divise_par
  return p_e , reste

ret=decomposer(33,5)
for i in ret:
    print i
autre_liste.append(["aymen","adem"])

print("display autre liste avec append")
for i in (autre_liste):
    print(i)

autre_liste.remove(["lll","world"])

print("display autre liste avec remove")
for i in (autre_liste):
    print(i)

autre_liste.append(["must","hello"])
del autre_liste[0]

print("display autre liste avec delete")
for i in (autre_liste):
    print(i)

print("length of autre liste is ", ma_liste1.__len__())

