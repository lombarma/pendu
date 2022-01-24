def morpion():
    plateau = [[" _ ", " _ ", " _ "],
               [" _ ", " _ ", " _ "],
               [" _ ", " _ ", " _ "]]
    for i in range(0, 3):
        for j in range(0, 3):
            print("|", end="")
            print(plateau[i][j], end="")
        print("|")
    print("-------------")

    continuer = True
    while continuer:
        xX = int(input("Joueur 1, saisir le numéro de la ligne : "))
        yX = int(input("Joueur 1, saisir le numéro de la colonne : "))
        if plateau[xX][yX] == " _ ":
            plateau[xX][yX] = " X "
            for i in range(0, 3):
                for j in range(0, 3):
                    print("|", end="")
                    print(plateau[i][j], end="")
                print("|")
            print("-------------")
        else:
            print("Case déjà utilisée.")
            continue

        for i in range(0, 3):
            if plateau[i].count(" X ") == 3 or plateau[i][0] == " X ":
                continuer = False

        xO = int(input("Joueur 2, saisir le numéro de la ligne : "))
        yO = int(input("Joueur 2, saisir le numéro de la colonne : "))
        if plateau[xO][yO] == " _ ":
            plateau[xO][yO] = " O "
            for i in range(0, 3):
                for j in range(0, 3):
                    print("|", end="")
                    print(plateau[i][j], end="")
                print("|")
            print("-------------")
        else:
            print("Case déjà utilisée.")
            continue

        for i in range(0, 3):
            if plateau[i].count(" O ") == 3:
                continuer = False


print(morpion())
