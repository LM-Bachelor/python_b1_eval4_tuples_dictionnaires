# EV 4 - Tuple et dictionnaires
# Exercice 1
import json

# 1. Auprès des utilisateurs, vous leur demanderez les informations suivantes :
# - nom
# - prénom
# - date de naissance au format jj/mm/aaaa
# - couleur préférée
# La saisie devra se faire au sein du terminal, à tout moment l'utilisateur pourra quitter la saisie en tapant le mot clé "stop"
# survey = []
# while True :
#     lastname = input("Nom :")
#     if lastname == "stop": break
#     firstname = input("Prénom :")
#     if firstname == "stop": break
#     date_of_birth = input("Date de naissance :")
#     if date_of_birth == "stop": break
#     color_prefered = input("Couleur préférée :")
#     if color_prefered == "stop": break

    # 2. Vous stockerez toutes ces informations dans un dictionnaire et vous l'ajouterez dans une liste « students »
    # data = {
    #     "lastname": lastname,
    #     "firstname": firstname,
    #     "date_of_birth": date_of_birth,
    #     "color_prefered": color_prefered
    # }
    # survey.append(data)

# # 3. Afin de garder ses information en mémoire, vous convertirez la liste en json l’enregistrerez dans un fichier « survey.json »
# with open("survey.json", "w") as data:
#     json.dump(survey, data)

f = open('survey.json')
survey = json.load(f)
# print(survey)

# 4.Une fois votre sondage terminé, vous vous apercevez que vous avez oublié de leur poser une question :
# « Combien d’animaux domestiques possède-vous ? ».
# Afin d’identifier la personne pour compléter votre liste, demandez à l’utilisateur son nom et son prénom,
# posez-lui la question et mettez à jour les données de votre fichier JSON
stop = False
while stop == False :
    stop = True
    lastname = input("Nom : ")
    firstname = input("Prénom : ")
    for data in survey:
        if(lastname == data['lastname'] and firstname == data['firstname']) :
            data['pets'] = int(input("Nombre d'animaux domestiques : "))

        # 5.La question « Combien d’animaux domestiques possède-vous ? » devra être posée tant que vous n’aurez pas récolté cette information pour tout le monde
        # if data.__contains__('pets') == False :
        #     stop = False
        for info in survey:
            if not('pets' in info.keys()):
                stop = False

with open("survey.json", "w") as data:
    json.dump(survey, data)

# 6.Prenez en compte que potentiellement il peut posséder un homonyme, si cela est le cas vous devrez lui demander sa date de naissance afin de pouvoir l’identifier correctement avant de lui poser la question.