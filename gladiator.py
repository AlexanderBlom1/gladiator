#Importera random
import random

#Lista med olika attacker
attacker = [("slag", 1, random.randint(0,10)), ("spark", 2, random.randint(0,10))]


#Variabler
dinHälsa = 5
fiendeHälsa = 5

#Funktioner för fiendes och dina attacker.
def fiendeAttack():
    
    attackFiende = random.choice(attacker)
    attackNamnFiende , attackSkadaFiende, chansFiende = attackFiende

def dinAttack():
    dittVal = input(f"Vilken attack vill du använda? 1.{attacker[0][0]} eller 2.{attacker[1][0]}: ")
    int(dittVal) == dittVal - 1
    attackDu = attacker[dittVal]
    attackNamnDu, attackSkadaDu, chansDu = attackDu


print("Välkommen till Colosseum, krigare!")
print("Du står i skuggan av de mäktiga murarna i den legendariska gladiatorarenan, där tusentals åskådare\nsamlats för att bevittna dagens blodiga spektakel. Solen steker över arenan, och dammet yr i luften\nmedan folkmassans rop ekar mellan väggarna. Ljudet av klingande svärd, sköldar som krossas, och\ntjutande triumf från tidigare matcher är fortfarande färskt i ditt sinne.")
