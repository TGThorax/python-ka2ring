# Oefening: Vraag de geboortedatum van de gebruiker en zeg de leeftijd.
huidig_jaar   = 2017
huidige_maand = 10
huidige_dag   = 24

jaar  = int(input("In welk jaar ben je geboren? "))
maand = int(input("En in welke maand? (getal) "))
# De dag moeten we pas weten als de geboortemaand deze maand is!
# Je kan het hier natuurlijk ook al vragen als je wilt.

leeftijd = huidig_jaar - jaar
if (maand > huidige_maand): # De gebruiker is nog niet verjaard
    leeftijd -= 1           # hetzelfde als "leeftijd = leeftijd - 1"
elif (maand == huidige_maand):
    dag = int(input("En welke dag? (getal) "))
    if (dag > huidige_dag):
        leeftijd -= 1
    elif (dag == huidige_dag):
        # leeftijd = leeftijd  # Dat doet helemaal niets natuurlijk
        print("Gelukkige verjaardag!")
#   else:                    # Enkel (dag < huidige_dag) kan nog =>
#                            # De gebruiker is al verjaard deze maand!
#       leeftijd = leeftijd  # Maar er hoeft niets veranderd te worden.
# else                   # De gebruiker is zeker al verjaard,
#                        # want enkel maand < huidige_maand kan nog!
#   leeftijd = leeftijd  # Maar we moeten niets aanpassen!
print("Dan ben je " + str(leeftijd) + " jaar oud.")



## Oefeningen zonder oplossing (mail bij vragen!).
#
# Oefening: start met leeftijd = huidig_jaar - jaar - 1 en verhoog die
#   waarde wanneer nodig. Vergelijk de voorwaarden daar met die hier.
#   Wat is het verschil in de tekens?
#
# Nog een oefening: kijk de waarden die de gebruiker ingeeft na.
#   Zorg ervoor je geen dag kan invoeren die later komt dan vandaag.
#   Probeer dat zo onafhankelijk mogelijk te doen van de bovenstaande code.
#
# Nadenkoefening: kan je bovenstaande 2 voorwaarden in de vorige opdracht uitvoeren
#   zonder in de  herhaling te vallen? (dat is geen uitdaging, maar een vraag!).
#   Als je toch iets mag aanpassen aan bovenstaande code, kan het dan?
#   Wat denk je dat de beste optie is?