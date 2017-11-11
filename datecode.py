import datetime
import time

print datetime.date.today()

year= input ("veuillez entrer l'annee de birthday  ")

a = datetime.date.today() - datetime.date(year, 1 ,1 )

print a.days/365

