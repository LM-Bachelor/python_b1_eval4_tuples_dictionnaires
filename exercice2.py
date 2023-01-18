# EV 4 - Tuple et dictionnaires
# Exercice 2
import json

# 1.Dans un premier temps, chargez votre fichier « survey.json » et convertissez-le en liste de dictionnaires
f = open('survey.json')
survey = json.load(f)

# 2.A partir de ce sondage, vous établirez un classement des couleurs les plus appréciées
# et pour chacune d’elle vous renverrez le nombre de personnes les appréciant
top_color = {}
for data in survey:
    if(data["color_prefered"] in top_color.keys()):
        top_color[data["color_prefered"]] += 1
    else:
        top_color[data["color_prefered"]] = 1
sorted_color = dict(sorted(top_color.items(), key=lambda item:item[1], reverse=True))
# print(sorted_color)

# 3.Afin de les remercier d’avoir participer à ce sondage, vous souhaiterez l’anniversaire des personnes fêtant leur anniversaire
# ce mois-ci avec la phrase suivante : « Le [jour] [mois en toute lettres] [Prénom] [Nom] fêtera ses [âge] ans »
import datetime
today = str(datetime.date.today())

months = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")
for data in survey:
    day_of_birth = data["date_of_birth"][0:2]
    month_of_birth = data["date_of_birth"][3:5]
    year_of_birth = data["date_of_birth"][6:10]

    # 4.Vous remarquerez une anomalie, en effet l’anniversaire de John Doe est déjà passé donc inutile de lui souhaiter.
    # A vous de modifier votre script pour ne pas prendre en compte les jours du mois déjà passés.
    if month_of_birth == today[5:7] and int(day_of_birth) >= int(today[-2:]):
        age = int(today[0:4]) - int(year_of_birth)
        print(f"Le {day_of_birth} {months[int(month_of_birth)-1]} {data['firstname']} {data['lastname']} fêtera ses {age} ans")
