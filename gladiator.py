import random
import os

#lista med svårighet
svårighet_lista = []

#Lista med mat
mat_lista = []

#Lista med karaktärer
Karaktärer_lista = []

line_breaker = 50

# lista med attacker
attacks = []
attacks_min = 0
attacks_max = -1
meny = False
mat_max = -1

#
rundor = 0



# Globl variabel
vald_karaktär = None

spel_status = True

# En klass där jag skappar olika mat objekt
class Mat:
    def __init__(self, namn, hälsa, chans):
        self.namn = namn
        self.hälsa = hälsa
        self.chans = chans

        mat_lista.append(self)

# En klass där jag skappar olika svårighets objekt
class Svårighet:
    def __init__(self, namn, multi):
        self.namn = namn
        self.multi = multi

        svårighet_lista.append(self)

# En klass där jag skappar olika attack objekt
class Attack:
    def __init__(self, namn, skada, chans, crit_skada, crit_chans):
        self.namn = str(namn)
        self.skada = skada
        self.chans = chans
        self.crit_skada = crit_skada
        self.crit_chans = crit_chans

        attacks.append(self)

# En klass där jag skappar olika karaktär objekt
class Karaktär:
    def __init__(self, namn, hälsa, crit_chans):
        self.namn = namn
        self.hälsa = hälsa
        self.crit_chans = crit_chans

        Karaktärer_lista.append(self)

class Block:
    def __init__(self, namn, chans):
        self.namn = namn
        self.chans = chans
        
# karaktärer  ( NAMN , HÄLSA , CRIT_CHANS )
du = Karaktär("du", 10, 10)

peter = Karaktär("Samnitus", 6, 75)
jörgen = Karaktär("Hoplomachus", 20, 15)
Magnus = Karaktär("Murmilo", 15, 45)

fiende = Karaktär("Dimachaerius", 10, 10)

# attacker  ( NAMN , SKADA , CHANS , CRIT_SKADA , CRIT_CHANS )
slag = Attack("slag", 1, 70, 2, 10)
spark = Attack("spark", 2, 50, 1.5, 10)

# blocker ( NAMN )
block = Block("block", 50)

# svårighet  ( NAMN , MULTI )
lätt = Svårighet("lätt", 0.5)
normalt = Svårighet("normalt", 1)
svårt = Svårighet("svårt", 2)

# mat
korv = Mat("Bröd", 2, 40)
gurka = Mat("Kyckling", 4, 50)
pickle = Mat("Vin", 6, 70)



# Går igenom mat listan så jag kan få ett max värde som random integer kan ta
for i in mat_lista:
    mat_max += 1
    

# Funktion för din attack
def din_attack():
    random_chans = random.randint(0, 100)
    random_crit_chans = random.randint(0, 100)

    # En loop som kollar ifall ditt svar finns i en lista
    while True:
        ditt_val = input(f"Vilken attack vill du välja?\n\n[Slag] - statistik \n-------------------------\nChans att träffa: {slag.chans}%\nSkada: {slag.skada}\nKritiskskada: {slag.crit_skada * slag.skada}\n-------------------------\n\n[Spark] - statistik\n-------------------------\nChans att träffa: {spark.chans}%\nSkada: {spark.skada}\nKritiskskada: {spark.crit_skada * spark.skada}\n-------------------------\nSVAR: \n\n").lower()
        giltig_attack = None

        for att in attacks:
            if att.namn.lower() == ditt_val.lower():
                giltig_attack = att  
                break

        if giltig_attack:
            attack_namn = giltig_attack.namn
            attack_skada = giltig_attack.skada
            attack_chans = giltig_attack.chans
            attack_crit_skada = giltig_attack.crit_skada
            attack_crit_chans = giltig_attack.crit_chans
            break

        else:
            print("Du valde en ogiltig attack. Försök igen.\n")

    # Kollar ifall du har prickat och gör kritisk skada
    if random_chans <= attack_chans:
        if random_crit_chans <= attack_crit_chans:
            print(f"Du valde {attack_namn} och gör {attack_skada * attack_crit_skada} kritisk skada")
            fiende.hälsa -= attack_skada * attack_crit_skada

        elif random_crit_chans > attack_crit_chans:
            print(f"Du valde {attack_namn} och gör {attack_skada} skada")
            fiende.hälsa -= attack_skada

    elif random_chans > attack_chans:
        print(f"Du valde {attack_namn} och missade")

# Blockera funktion
def blockera():
    global du, fiende
    random_chans = random.randint(0, 100)
    
    # Visar att du valde blockering
    print("Du valde att blockera!")

    # Blockera fiendens attack om blocken träffar
    if random_chans <= block.chans:
        print(f"Blockering lyckades! Du blockerade fiendens attack!")
        # Blockeringen blockerar skada helt, så vi återvänder här och stoppar fiendens attack
        return  

    else:
        print(f"Blockering misslyckades! Fienden lyckades träffa dig!")
        fiende_attack()  # Om blocket misslyckas, kommer fienden att attackera


# For loop som går igenom listan med attacker och gör ett max värde som random kan ta
for att in attacks:
    attacks_max += 1

# Funktion för fiendens random attack
def fiende_attack():
    global vald_karaktär

    random_attack = random.randint(attacks_min, attacks_max)
    random_chans = random.randint(0, 100)
    random_crit_chans = random.randint(0, 100)

    fiende_attack_crit_chans = fiende.crit_chans

    fiende_attack = attacks[random_attack]
    fiende_attack_namn = fiende_attack.namn
    fiende_attack_skada = fiende_attack.skada * svårighet_multi
    fiende_attack_chans = fiende_attack.chans
    fiende_attack_crit_skada = fiende_attack.crit_skada
    fiende_attack_crit_chans = fiende_attack.crit_chans

    # Kollar ifall fiende har prickat och kritisk skada
    if random_chans <= fiende_attack_chans:
        if random_crit_chans <= fiende_attack_crit_chans:
            print(f"Fiende valde {fiende_attack_namn} och gör {fiende_attack_skada * fiende_attack_crit_skada} kritisk skada")
            du.hälsa -= fiende_attack_skada * fiende_attack_crit_skada

        elif random_crit_chans > fiende_attack_crit_chans:
            print(f"Fiende valde {fiende_attack_namn} och gör {fiende_attack_skada} skada")
            du.hälsa -= fiende_attack_skada

    elif random_chans > fiende_attack_chans:
        print(f"Fiende valde {fiende_attack_namn} och missade")


# En funktion som triggrar efter varje runda som ger dig ett val om du vill äta en sak eller inte
def random_event():
    random_chans = random.randint(0,100)

    if random_chans < 10:
        random_mat = random.randint(0, mat_max)

        mat = mat_lista[random_mat]
        
        mat_namn = mat.namn
        mat_hälsa = mat.hälsa
        mat_chans = mat.chans

        print(f"Plötsligt kommer en {mat_namn} från himlen och landar på marken!")
        ditt_mat_val = input(f"Vill du konsumera {mat_namn}?\nDu kommer att få {mat_hälsa} hälsa, men du har en {mat_chans}% chans att fienden attackerar dig när du äter.\nSvar[JA/NEJ]: ")

        if ditt_mat_val.lower() == "ja":
            du.hälsa += mat_hälsa
            print(f"Du åt {mat_namn} och återhämtade dig! Du har nu {du.hälsa} hälsa.")
            
            if random_chans < mat_chans:
                print("Men medan du äter, slår fienden till!")
                fiende_attack()
        
        else:
            print(f"Eftersom du inte konsumerade {mat_namn}, försvinner den och du missar chansen att återhämta dig.")
            
# En funktion som änrar fiendens hälsa pågrund av svårighet
def svårighets_grad():
    fiende.hälsa *= svårighet_multi

print(f"Mat max: {mat_max}")

# ----------------------------------------------------- meny ----------------------------------------------------- #

while True:
        print("\n" + "-" * line_breaker)
        ditt_val = input(f"Vilken svårighet vill du köra? \n Lätt - fiendens hälsa och skada kommer att multipleceras med {lätt.multi}\n Normalt - fiendens hälsa och skada kommer att multipliceras med {normalt.multi}\n Svårt - fiendens hälsa och skada kommer att multipliceras med {svårt.multi}\n SVAR: ")
        print("-" * line_breaker + "\n\n")
        giltig_svårighet = None

        for svår in svårighet_lista:
            if svår.namn.lower() == ditt_val.lower():
                giltig_svårighet = svår
                break

        if giltig_svårighet:
            svårighet_multi = giltig_svårighet.multi
            print(f"Du valde {giltig_svårighet.namn}")
            break

        else:
            print("Du valde en ogiltig svårighet. Försök igen!\n")

while True:
        print("\n" + "-" * line_breaker)
        ditt_val = input(f"Vilken karaktär vill du används?\n Samnitus - Hälsa: {peter.hälsa} Kritisk chans:{peter.crit_chans}\n Hoplomachus - Hälsa: {jörgen.hälsa} Kritisk chans: {jörgen.crit_chans}\n Murmilo - Hälsa: {Magnus.hälsa} Kritisk chans: {Magnus.crit_chans} \n SVAR: ")
        print("-" * line_breaker + "\n\n")
        giltig_karaktär = None

        for karak in Karaktärer_lista:
            if karak.namn.lower() == ditt_val.lower():
                giltig_karaktär = karak
                break

        if giltig_karaktär:
            crit_chance = giltig_karaktär.crit_chans
            hälsa = giltig_karaktär.hälsa
            
            slag.crit_chans = crit_chance
            spark.crit_chans = crit_chance

            du.hälsa = hälsa
            du.crit_chans = crit_chance

            vald_karaktär = giltig_karaktär

            print(f"Du valde {giltig_karaktär.namn}")


            break

        else:
            print("Du valde en ogiltig karaktär. Försök igen!\n")

# ---------------------------------------------------------------------------------------------------------------- #

svårighets_grad()


# --------------------------------------------------- spel-loop --------------------------------------------------- #

while spel_status:
    if du.hälsa > 0 and fiende.hälsa > 0:
        
        print(f"Du har {du.hälsa} hälsa kvar och {du.crit_chans} kritsk chans. Din fiende har {fiende.hälsa} hälsa kvar och {fiende.crit_chans} kritisk chans\n")
        print("-" * line_breaker + "\n")

        while not meny:
            print("Vad vill du göra detta drag")
            menyVal = input("1. Attackera \n2. Blockera \n3. Avsulta \n ")
            if menyVal == "1":
                meny = True
                din_attack()
                fiende_attack()

            elif menyVal == "2":
                blockera()
                meny = True
            elif menyVal == "3":
                meny = True
                spel_status = False

        print("\n" + "-" * line_breaker + "\n")

       
        print("\n" + "-" * line_breaker + "\n")
        random_event()

        meny = False

        rundor += 1

    else:
        if du.hälsa <= 0 or rundor >= 15:
            print("Du förlorade")
            spel_status = False

        elif fiende.hälsa <= 0 or rundor >= 15:
            print("Du vann")
            spel_status = False

# --------------------------------------------------------------------------------------------------------------- #
