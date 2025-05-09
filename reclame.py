from algemene_functies import mijn_functie_2

def aanbieding_1(reclame1):
  smaak, originele_prijs, korting = reclame1
  nieuwe_prijs = originele_prijs - (korting * originele_prijs)
  return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {originele_prijs} Euro voor {nieuwe_prijs:.2f} Euro."

reclame1 = ["aardbei", 4, 0.1]
print(aanbieding_1(reclame1))

def inkomsten_totaal(inkomsten, btw):
  totaal = sum(inkomsten)
  btw_bedrag = totaal * btw
  return f"Het totaal van alle inkomsten van deze week is {totaal} Euro, waarover {btw_bedrag} Euro BTW betaald moet worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09
print(inkomsten_totaal(inkomsten, btw))

def laag_en_hoog(mijn_lijst):
  return max(mijn_lijst), min(mijn_lijst)
def gemiddelde(mijn_lijst):
  average = sum(mijn_lijst) / len(mijn_lijst)
  return f"De gemiddelde inkomsten deze week zijn {average:.2f} Euro."

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(mijn_lijst))
print(gemiddelde(mijn_lijst))

def meervoudig(invoer_lijst):
  return (laag_en_hoog(invoer_lijst))

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
  korte_lijst = laag_en_hoog(invoer_lijst_2)
  return mijn_functie_2([korte_lijst])

invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]
print(combinatie(invoer_lijst_2))