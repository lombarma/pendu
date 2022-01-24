from random import choice

clearConsole5 = lambda: print("\n" * 5)
clearConsole2 = lambda: print("\n" * 2)
clearConsole3 = lambda: print("\n" * 3)

HANGMANPICS = ['''






=========''', '''

      |
      |
      |
      |
      |
=========''', '''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def read_file(filename):
    file = open(filename, 'r', encoding='utf8')
    liste = file.read().split("\n")
    file.close()
    return liste


def question():
    a = int(
        input("1 ---> Jouer tout seul avec un mot aléatoire\n2 ---> Jouer à deux\nSaisissez ici votre réponse : "))
    if a == 2:
        clearConsole2()
        mot_a_trouver = str(input("Entrer le mot à trouver : ")).strip()
        clearConsole5()
        clearConsole5()
        clearConsole5()
        clearConsole5()
        print(pendu(mot_a_trouver))
    elif a == 1:
        try:
            liste_mots = read_file(r"C:\Users\Maxime\Desktop\ESIEE\E2\PythonE2\data\mots.txt")
            mot_aleatoire = choice(liste_mots)
            print(pendu(mot_aleatoire))
        except FileNotFoundError:
            print("La bibliothèque de mots n'est pas disponible. Vous ne pouvez jouer qu'à deux.")
            return question()
    else:
        print("Choisissez entre 1 et 2.")
        return question()


def pendu(mot):
    plateau = [" _ " for i in range(len(mot))]
    chances = -1
    essais = 10
    print('\n' + "".join(plateau) + '\n\n')
    lettres_fausses = []

    while "".join(plateau) != mot:
        lettre = str(input("Lettre : "))

        if len(lettre) > 1:
            print("Une lettre à la fois")
            pass

        if lettre in mot:
            for index, letter in enumerate(mot):
                if letter == lettre:
                    plateau[index] = lettre
            print(HANGMANPICS[chances])
            print(f"\nEssais restants : {essais} \n")
            print("".join(plateau) + '\n')

        elif lettre not in mot:
            chances += 1
            essais -= 1
            if len(lettre) == 1:
                lettres_fausses.append(lettre)
                print(HANGMANPICS[chances])
                print(f"\nMauvaise réponse. Essais restants : {essais} \n")
            print("".join(plateau) + '\n')
            if essais == 0:
                return f"C'est perdu, le mot à trouver était '{mot}'.\n\n"
        print(f"Lettres fausses essayées : {lettres_fausses} \n")

        clearConsole5()

        if "".join(plateau) == mot:
            return f"C'est gagné !!! \n\n\n\n"


print(question())
