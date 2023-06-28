import random, random, os, csv, colorama, keyboard
from colorama import Fore
os.system('cls')
with open("password.csv", mode="a", newline="") as fichier:
    writer = csv.writer(fichier)
while True:
    print(Fore.RED + '----------------------------------------------------------------------------------------------------------------------')    
    print(" ___  _  _    ____    __    ___  ___  _    _  _____  ____  ____  ")
    print("/ __)( \/ )  (  _ \  /__\  / __)/ __)( \/\/ )(  _  )(  _ \(  _ \ ")
    print("\__ \ )  (    )___/ /(__)\ \__ \\__ \ )    (  )(_)(  )   / )(_) ) ")
    print("(___/(_/\_)  (__)  (__)(__)(___/(___/(__/\__)(_____)(_)\_)(____/ ")
    print('  ')                  
    print(Fore.RED + '----------------------------------------------------------------------------------------------------------------------')    
    print(Fore.RESET + '  ')
    print(Fore.RESET + '[1] Adresse Mail')    
    print(Fore.RESET + '  ')
    print(Fore.RESET + "[2] Nom d'utilisateur ")    
    print(Fore.RESET + '  ')
    print(Fore.RED + '----------------------------------------------------------------------------------------------------------------------')    
    print(Fore.RESET + '  ')

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbol = "![]()*;/,.-_"
    nom_fichier = "password.csv"
    all = lower + upper + numbers + symbol
    all2 = lower + numbers
    length = random.randint(16, 32)
    password = "".join(random.sample(all,length))
    user = "".join(random.sample(all2,length))

    choix = ""
    while True:
        if keyboard.is_pressed("1"):
            choix = "1"
            break
        elif keyboard.is_pressed("2"):
            choix = "2"
            break
        else:
            continue

    if keyboard.is_pressed("1") or keyboard.is_pressed("2"):
        if keyboard.is_pressed("1"):
            email=input("Entrez l'adresse mail utilisée : ")
            site =input("Entrez le site concerné  (ne pas oublier le .comfr) : ")
            length = random.randint(16, 32)
            password = "".join(random.sample(all,length))
            print(Fore.RESET + '  ')
            print(Fore.GREEN + site, Fore.RESET + "|", Fore.BLUE + "User :", Fore.RESET + user, "|", Fore.BLUE + "Password :", Fore.RESET + password)
            print(Fore.RESET + '  ')
            print(Fore.RESET + "https://"+site)
            nouvelles_donnees = [[site, email, password]]
            with open("password.csv", mode="r") as fichier:
                reader = csv.reader(fichier)
                entrees_existantes = {}
                for ligne in reader:
                    # Vérifier si la ligne contient suffisamment de valeurs avant d'essayer d'accéder à l'index
                    if len(ligne) > 0:
                        entrees_existantes[ligne[0]] = ligne
                with open("password.csv", mode="w", newline="") as fichier:
                    writer = csv.writer(fichier)
                    for ligne in nouvelles_donnees:
                        if ligne[0] in entrees_existantes:
                            entrees_existantes[ligne[0]] = ligne
                        else:
                            entrees_existantes[ligne[0]] = ligne
                    for ligne in entrees_existantes.values():
                        writer.writerow(ligne)
                print(Fore.RESET + '  ')
                print("Les nouvelles données ont été ajoutées et les entrées existantes ont été mises à jour dans le fichier CSV.")
                print(Fore.RESET + '  ')
                chemin_absolu = os.path.abspath(nom_fichier)
                print(f"Le fichier CSV a été créé avec succès au chemin suivant : {chemin_absolu}")
                print(Fore.RESET + '  ')

        elif keyboard.is_pressed("2"):
            user=input("Entrez le nom d'utilisateur : ")
            site =input("Entrez le site concerné  (ne pas oublier le .comfr) : ")
            length = random.randint(16, 32)
            password = "".join(random.sample(all,length))
            print(Fore.RESET + '  ')
            print(Fore.GREEN + site, Fore.RESET + "|", Fore.BLUE + "User :", Fore.RESET + user, "|", Fore.BLUE + "Password :", Fore.RESET + password)
            print(Fore.RESET + '  ')
            print(Fore.RESET + "https://"+site)
            nouvelles_donnees = [[site, user, password]]
            with open("password.csv", mode="r") as fichier:
                reader = csv.reader(fichier)
                entrees_existantes = {}
                for ligne in reader:
                    # Vérifier si la ligne contient suffisamment de valeurs avant d'essayer d'accéder à l'index
                    if len(ligne) > 0:
                        entrees_existantes[ligne[0]] = ligne
                with open("password.csv", mode="w", newline="") as fichier:
                    writer = csv.writer(fichier)
                    for ligne in nouvelles_donnees:
                        if ligne[0] in entrees_existantes:
                            entrees_existantes[ligne[0]] = ligne
                        else:
                            entrees_existantes[ligne[0]] = ligne
                    for ligne in entrees_existantes.values():
                        writer.writerow(ligne)
                print(Fore.RESET + '  ')
                print("Les nouvelles données ont été ajoutées et les entrées existantes ont été mises à jour dans le fichier CSV.")
                print(Fore.RESET + '  ')
                chemin_absolu = os.path.abspath(nom_fichier)
                print(f"Le fichier CSV a été créé avec succès au chemin suivant : {chemin_absolu}")
                print(Fore.RESET + '  ')


    else:
        break
