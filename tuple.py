def afficher_flottant(flottant):
    if type(flottant) is not float:
        raise TypeError(" LE parametre attendue doit etre un float")
    flottant=str(flottant)
    p_e,p_f=flottant.split(".")
    return ",".join([p_e,p_f[:3]])

print(afficher_flottant(5.88888))

a="hello World"
print(a[:2])


def fonction_inconnue(*parametres):
    print("j'au recu {} ".format(parametres))

fonction_inconnue(44,'r',66,"fdfdf")


def afficher(sep=' ',fin='\n',*parametres1):
    parametres1=list(parametres1)
    for i, parametre in enumerate(parametres1):
        parametres1[i]=str(parametre)
    chaine= sep.join(parametres1)
    chaine+=fin



inventaire = [(" pommes ", 22) ,(" melons ", 4) ,(" poires ", 18) ,(" fraises ", 76) ,(" prunes ", 51) ,]

for fruit,qt in inventaire:
    print(fruit.strip(),qt)
