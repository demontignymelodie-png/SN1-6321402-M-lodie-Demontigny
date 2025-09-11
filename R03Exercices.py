def saluer(nom='inconnu'):
    print(f'Bonjour, {nom} !')
saluer()

def temp(celcius):
    return celcius * 9 / 5 + 32

celcius=float(input('sasir une temperature en celcius : '))
resultat=temp(celcius)
print(f'{celcius} degree celcius correspond a {resultat} farenheit')






