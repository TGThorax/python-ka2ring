# Oefening: maak een programma dat je BMI geeft
lengte  = int(input("Geef je lengte in cm: "))
gewicht = int(input("Geef je gewicht in kg: "))
if (lengte <= 0):
    print("Fout: lengte kan niet kleiner of gelijk zijn aan nul. Gegeven: " + str(lengte) + ".")
elif (gewicht <= 0):
    print("Fout: gewicht kan niet kleiner of gelijk zijn aan nul. Gegeven: " + str(gewicht) + ".")
else:
    lengte /= 100 # van cm naar m
    bmi = (gewicht / lengte**2)
    print("Je BMI is: " + str(round(bmi, 2)))

## Oefeningen zonder oplossing (mail bij vragen!)
#
# Oefening: zorg ervoor dat het programma direct stopt als een foutieve lengte gegeven wordt.
#   Vraag in dat geval dus niet naar het gewicht.