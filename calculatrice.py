historique_calculs = []

def operator():
    while True:
        try:
            a = float(input("Saisissez un premier chiffre/nombre: "))
            operateur = input("Entrez l'opérateur (+, -, *, /, %): ")
            b = float(input("Saisissez un deuxième chiffre/nombre: "))

            result = None

            if operateur == "+":
                result = a + b
            elif operateur == "-":
                result = a - b
            elif operateur == "*":
                result = a * b
            elif operateur == "/":
                result = a / b
            elif operateur == "%":
                result = a % b

            if result is not None:
                historique_calculs.append((a, operateur, b, result))
                print("Résultat:", result)
                return result

        except ValueError:
            print("Erreur de saisie. Veuillez entrer des nombres valides.")

def retry():
    while True:
        try_again = input("Voulez-vous faire un autre calcul ? (oui/non): ")
        if try_again.lower() == "oui":
            operator()
        else:
            print("D'accord, au revoir !")
            break

def afficher_historique():
    h = input("Voulez-vous afficher l'historique de vos calculs ? (oui/non): ")
    if h.lower() == "oui":
        if historique_calculs:
            print("Historique des calculs:")
            for calcul in historique_calculs:
                print(f"{calcul[0]} {calcul[1]} {calcul[2]} = {calcul[3]}")
        else:
            print("L'historique est vide.")

operator()
retry()
afficher_historique()