while True:
 try:
  annee = input () # On demande l ' utilisateur de saisir
  annee = int ( annee ) # On essaye de convertir l ' ann  en un entier

 except (NameError,SyntaxError) as exept:
    print "feel the correct data", exept
 else:
  print "in case of"

 finally:
   print" je m'execute quelque soit le resultat"

#pass  ne rien faire , ajouter avec except