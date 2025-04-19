import random
import os
import csv
from colorama import Fore
import keyboard

os.system('cls')

def afficher_menu():
    print(Fore.RED + '-' * 118)
    print(" ___  _  _    ____    __    ___  ___  _    _  _____  ____  ____  ")
    print("/ __)( \/ )  (  _ \\  /__\\  / __)/ __)( \\/\\/ )(  _  )(  _ \\(  _ \\ ")
    print("\\__ \\ )  (    )___/ /(__)\\ \\__ \\\\__ \\ )    (  )(_)(  )   / )(_) ) ")
    print("(___/(_/\\_)  (__)  (__)(__)(___/(___/(__/\\__)(_____)(_)/_)(____/ ")
    print('  ')
    print(Fore.RED + '-' * 118)
    print(Fore.RESET + '  ')
    print(Fore.RESET + '[1] Adresse Mail')
    print(Fore.RESET + '  ')
    print(Fore.RESET + "[2] Nom d'utilisateur ")
    print(Fore.RESET + '  ')
    print(Fore.RED + '-' * 118)
    print(Fore.RESET + '  ')

def generer_password(length, charset):
    return "".join(random.sample(charset, length))

def sauvegarder_donnees(nom_fichier, nouvelles_donnees):
    with open(nom_fichier, mode="r") as fichier:
        reader = csv.reader(fichier)
        entrees_existantes = {ligne[0]: ligne for ligne in reader if len(ligne) > 0}
    with open(nom_fichier, mode="w", newline="") as fichier:
        writer = csv.writer(fichier)
        for ligne in nouvelles_donnees:
            entrees_existantes[ligne[0]] = ligne
        writer.writerows(entrees_existantes.values())
    print(Fore.RESET + '  ')
    print("Les nouvelles données ont été ajoutées et les entrées existantes ont été mises à jour dans le fichier CSV.")
    print(Fore.RESET + '  ')
    print(f"Le fichier CSV a été créé avec succès au chemin suivant : {os.path.abspath(nom_fichier)}")
    print(Fore.RESET + '  ')

def main():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbol = "![]()*;/,.-_"
    all_chars = lower + upper + numbers + symbol
    all2_chars = lower + numbers
    nom_fichier = "password.csv"

    while True:
        afficher_menu()
        choix = ""
        while not choix:
            if keyboard.is_pressed("1"):
                choix = "1"
            elif keyboard.is_pressed("2"):
                choix = "2"

        site = input("Entrez le site concerné (ne pas oublier le .comfr) : ")
        length = random.randint(16, 32)
        password = generer_password(length, all_chars)

        if choix == "1":
            email = input("Entrez l'adresse mail utilisée : ")
            print(Fore.GREEN + site, Fore.RESET + "|", Fore.BLUE + "Email :", Fore.RESET + email, "|", Fore.BLUE + "Password :", Fore.RESET + password)
            nouvelles_donnees = [[site, email, password]]
        elif choix == "2":
            user = input("Entrez le nom d'utilisateur : ")
            print(Fore.GREEN + site, Fore.RESET + "|", Fore.BLUE + "User :", Fore.RESET + user, "|", Fore.BLUE + "Password :", Fore.RESET + password)
            nouvelles_donnees = [[site, user, password]]

        print(Fore.RESET + "https://" + site)
        sauvegarder_donnees(nom_fichier, nouvelles_donnees)

if __name__ == "__main__":
    main()
