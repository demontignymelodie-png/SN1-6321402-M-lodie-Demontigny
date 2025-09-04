
celcius=float(input('sasir une temperature en celcius : ')) #50.0
resultat = celcius * 9 / 5 + 32
print(f'{celcius} degree celcius corresponds a {resultat} farenheit')

largeur=float(input('saisir une unite en largeur : ')) #20.0
longueur=float(input('saisir une unite en longueur : ')) #30.0
resultat = largeur * 2 + longueur * 2
print(f'{largeur} unite de largeur et {longueur} unite de longueur correspond a {resultat} unite de perimetre')

chiffre=int(input('saisir un chiffre entre 1 et 9 : '))
decimal=int(input('saisir une decimal : '))
resultat = chiffre / 10 ** decimal
print(f'reponse : {resultat}')

minimal= int(input('saisir un nombre minimal'))
maximal= int(input('saisir un nombre maximal'))
resultat = (random.randint(minimal,maximal))
print(f'reponse : {resultat}')



