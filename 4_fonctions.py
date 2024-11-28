
"""
#job 1

def My_print_hello():
    print("Hello world")

My_print_hello()

#job 2

def My_print_name(name):
    print(name)

My_print_name("Mehmet")
My_print_name("Ali")

#job 3

def add(x, y):
    print(x + y)

add(3, 7)
add(44, 56)

#job 4

def GetHello():
    return "Hello la Platforme"

print(GetHello())


#job 5

def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "division par zero"
    elif operator == "%":
            return num1 % num2
    else:
        return "mauvaise operation"


print(calcule(3, "+", 2))
print(calcule(3, "-", 0))
print(calcule(3, "*", 2))
print(calcule(3, "/", 2))
print(calcule(3, "/", 0))
print(calcule(3, "%", 2))



#job 6

def verification(nombre):
    if nombre > 0:
        return f"{nombre} est positif."
    elif nombre < 0:
        return f"{nombre} est negatif."
    else:
        return f"{nombre} n'est ni positif ni negatif"

print(verification(0))
print(verification(5))
print(verification(-7))

#job 7

def codage(langage):
    if langage == "Javascript":
        return "tu es un développeur web"
    elif langage == "python":
        return "tu es un développeur IA"
    elif langage == "java":
        return "tu es un développeur logiciel"
    elif langage == "reactjs":
        return "tu es un développeur mobile"
    else :
        return "unjour,je serai le meilleur développeur…"

print(codage("python"))
print(codage(""))

#job 8

def primeur(type, saison):
    if type == "fruit" and saison == "hiver":
        return "Orange, mandarine et kiwi"
    elif type == "fruit" and saison == "été":
        return "Poire, fraise et cassis"
    elif type == 'légume' and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "légume" and saison == "été":
        return "artichaut, aubergine, navet"
    else:
        return "mauvais saisi"

print(primeur("fruit", "été"))

#job 9

def moyenne(): 
    a = int(input("Enter your first grade: "))
    b = int(input("Enter your second grade: "))
    c = int(input("Enter your third grade: "))
    
    moyenne_etudiant = (a + b + c) / 3
    print(f"La moyenne est : {moyenne_etudiant:.2f}")
    
    if 15 <= moyenne_etudiant <= 20:
        return "Très bon élève"
    elif 11 <= moyenne_etudiant < 15:
        return "Bon élève"
    elif 8 <= moyenne_etudiant < 11:
        return "Élève moyen"
    elif 0 <= moyenne_etudiant < 8:
        return "Élève devant faire des efforts"
    else:
        return "Mauvaise saisie"

# Çağırdığınızda sonucu ekrana bastırabilmek için print ile çağırıyoruz

print(moyenne())


"""
#job 10
def nombre(num):
    num_ent = int(num)
    if num_ent > 0:
        return f"{num_ent} est un nombre entier et positif."
    else:
        return f"{num_ent} est soit négatif soit n'est pas un nombre entier."

# Demander 3 fois une entrée à l'utilisateur
for i in range(3):  # La boucle s'exécute 3 fois
    user_input = input(f"({i+1}/3) Entrez un nombre : ")
    try:
        print(nombre(user_input))
    except ValueError:
        print("Veuillez entrer un nombre valide.")

print("Programme terminé après 3 essais.")

#job 11

def time_to_text():
    
    # Demander le nombre entier de minutes à l'utilisateur
    minutes = int(input("Veuillez entrer un nombre entier de minutes : "))
    
    # Calculer les heures et les minutes restantes
    heures = minutes // 60  # Division entière pour obtenir les heures
    minutes_restantes = minutes % 60  # Le reste correspond aux minutes restantes

    # Construire la chaîne de caractères à afficher
    resultat = f"{heures} heure{'s' if heures > 1 else ''} et {minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}"
    
    # Afficher le résultat
    print(resultat)
time_to_text()

    # pour aller plus loin.
def inverser_chaine(chaine):
    # Utiliser le slicing pour inverser la chaîne
    return chaine[::-1]

# Exemple d'utilisation
mot = "nikana"
mot_inverse = inverser_chaine(mot)
print(f"Le mot inversé de '{mot}' est '{mot_inverse}'")

