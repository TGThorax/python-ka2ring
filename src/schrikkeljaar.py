# Maak een programma dat aangeeft of een gegeven jaar een schrikkeljaar is.

# Een jaar is een schrikkeljaar als:
#   het deelbaar is door 4
#   maar niet door 100
#   maar weer wel door 400
# Anders gezegd: een jaar is GEEN schrikkeljaar als:
#   het niet deelbaar is door 4
#   en anders: het is wel deelbaar door 100, maar niet door 400.
#   (noot: als iets deelbaar is door 100 of 400, is het ook deelbaar door 4).
jaar     = int(input("Geef een jaar: "))
antwoord = "Het jaar " + str(jaar) + " is "
if ((jaar % 4 != 0) or (jaar % 100 == 0 and jaar % 400 != 0)):
    antwoord += "g"
antwoord += "een schrikkeljaar."
print(antwoord)

## Oefeningen zonder oplossing (mail bij vragen!).
#
# Wiskundige oefening:
#   Stel dat een schrikkeljaar gedefinieerd is voor de getallen p, q en r als volgt:
#   "Een schrikkeljaar is een jaar dat deelbaar is door p, maar niet als het
#    deelbaar is door q, maar weer wel als het deelbaar is door r".
#   Hoe zou je het programma aanpassen?
#   Hint:
#   Probeer bijvoorbeeld enkele priemgetallen voor p,q,r: p = 5, q = 13, r = 23
#   Hint:
#   Bovenstaande programma vertrouwt erop dat als n deelbaar is door 400
#     (of 100) dan is n ook deelbaar door 4. Met willekeurige p, q, r is dat niet zo!
#   Mogelijke hint:
#   bovenstaande code is ook equivalent met bijvoorbeeld
#     if (jaar % 4 == 0):
#         if (jaar % 100 == 0 and jaar % 400 != 0):
#             antwoord += "g"
#     else: # niet deelbaar door 4
#         antwoord += "g"