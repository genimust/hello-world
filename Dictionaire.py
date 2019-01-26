mon_dict=dict()

a=str()
print (type(a))

mon_dict["pseudo"]="genimust"
mon_dict["Password"]="*"
mon_dict["Telephone"]="055555"
print(mon_dict)


def parcour_key():
  print("#### Parcourir le des KEYS ########")
  for cle in mon_dict.keys():
    print(cle)
  print("####        FIN DE PARCOUR  de KEYS ########")

def parcour_value():
  print("#### Parcourir le des value ########\n")
  for value in mon_dict.values():
    print(value)
  print("####        FIN DE PARCOUR  de value ########\n")


try:
    print(mon_dict["pseudo"])
except KeyError :
    print("KEy dont exist ")

print(mon_dict.pop("Password"))
print(mon_dict)

parcour_key()
parcour_value()
