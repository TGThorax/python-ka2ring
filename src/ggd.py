# Maak een programma dat de grootste gemene deler van twee getallen geeft.

# We gebruiken het algoritme van Euclides:
#   ggd van a en b == ggd van b en (a rest b). Stop als b = 0.
def ggd(a, b):
    return (a if b == 0 else ggd(b, a % b))

# bovenstaande is hetzelfde als:
def ggd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

## Oefeningen zonder oplossing (mail bij vragen!).
#
# Denkoefening:
#   Werkt het algoritme voor negatieve getallen?
#   Probeer het in alle combinaties (a=+ en b=-, a=- en b=+, a=- en b=-)
#   Wat moet je doen als je ervoor wilt zorgen dat altijd geldt dat ggd symmetrisch is,
#     m.a.w. dat ggd(a, b) == ggd(b, a) voor alle a en b, ook negatieve?
#
# Denkoefening:
#   Wat gebeurt er in de eerste stap als b > a?
#   HINT: dan zal a % b = a
#
# Denkoefening:
#   Wat denk je dat er gebeurt als je kommagetallen ingeeft die een veelvoud zijn van elkaar?
#   Wat als je kommagetallen geeft die dat niet zijn? Wat is het antwoord volgens jou? Wat volgens de computer?
#   Maakt het wiskundig wel steek om de ggd van kommagetallen te nemen?
#   Kan je verklaren waarom de computer zo'n antwoord geeft? (Als je dat niet kan, is dat helemaal niet zo erg want we
#     hebben kommagetallen tot nu toe niet grondig bestudeerd)
# Wiskundige oefening: