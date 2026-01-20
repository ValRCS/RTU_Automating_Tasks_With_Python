# Plāns šodiena
# Apskatīt saraksta datu struktūru Python valodā
# apskatīt teksta failus un to apstrādi Python valodā

print("Plāns šodienai:")
print("- Apskatīt saraksta datu struktūru Python valodā")
print("- Apskatīt teksta failus un to apstrādi Python valodā")

# Kāpēc vajdzīgi saraksti?

# mēs tāču mākam izmantot mainīgos, vai ne?
# piemēram:
a1 = "Oskars"
a2 = "Jānis"
a3 = "Pēteris"
a4 = "Anna"

print(a1)
print(a2)
print(a3)
print(a4)

# ko darīt ja mums jāglabā 1000 vārdi?
# vai 10 000 vārdi?
# vai pat 1 000 000 vārdi?
# vai vēl vairāk?

# risinājums ir saraksti (lists)
# saraksti ir datu struktūra, kas ļauj glabāt vairākas vērtības vienā mainīgajā
# saraksti ir ļoti ērti, jo mēs varam piekļūt katrai vērtībai pēc tās indeksa
# varam sarakstus mainīt, pievienot jaunus elementus, dzēst elementus utt.
# saraksti ir ļoti elastīgi un ērti lietojami

# sāksim ar tukšu sarakstu
saraksts = [] # tātad kvadrātiekavās norādām, ka tas ir saraksts

# cik mums tur ir elementu?
print(f"Sarakstā ir {len(saraksts)} elementi.")

# pievienosim vienu elementu
saraksts.append("Oskars") # append modificē sarakstu, pievienojot tam jaunu elementu beigās
print(f"Sarakstā ir {len(saraksts)} elementi.")
# pieliksim arī Valdis
saraksts.append("Valdis")
print(f"Sarakstā ir {len(saraksts)} elementi.")
# un tagad apskatīsim visu sarakstu
print(saraksts)

# man varētu būt skaitļu saraksts to ir viegli uztaisit ar list un range
# piemēram no 0 līdz 19
skaitli = list(range(20)) # tātad pusgatavos skaitļus no range mēs pārvēršam par sarakstu ar list
print(skaitli)

# piekļuve individuāliem elementiem sarakstā
# tam izmanot indeksu līdzigi string indeksime, abos pirmais elements ir ar indeksu 0
print(saraksts[0]) # pirmais elements
print(saraksts[1]) # otrais elements

#kā būta ja mēģinātu piekļūt 3 elementam ar indeksu 2?
# print(saraksts[2]) # šeit būskļūda jo sarakstā ir tikai 2 elementi ar indeksiem 0 un 1

# ja neesam pārliecināti cik elementu ir sarakstā, varam izmantot len funkciju
elementu_skaits = len(saraksts) # to jau zinam un tad if nosacījumā pārbaudīt
if elementu_skaits > 2: # mēs prasam atļauju vispirms
    print(saraksts[2]) # šeit vairs nebūs kļūda jo zinām ka ir vairāk par 2 elementiem
else:
    print("Sarakstā nav tik daudz elementu.")

# otrs veids būtu ar try except
try: # šeit mēs tā teikt "šaujam" vispirms un prasam piedošanu ja kļūda
    print(saraksts[2]) # mēģinam piekļūt 3 elementam
except IndexError:
    print("Noķērām kļūdu. Sarakstā nav tik daudz elementu.") # ja ir kļūda, izpildās šis bloks

# pieliksim Līgu sarakstam
saraksts.append("Līga") # pievienojam vēl vienu elementu
print(saraksts)
# tagad nebūs vairs kļūdas piekļūstot 3 elementam
print(saraksts[2]) # šeit viss ir kārtībā jo sarakstā ir tagad 3 elementi

# tagad piekļusim 3 jam skaitlim
print(skaitli[2]) # šeit viss ir kārtībā jo skaitļu sarakstā ir daudz elementu

# pēdējais elements
# mēs varētu darīt šādi rēķinat garumu un atņemt 1
print(saraksts[len(saraksts)-1]) # sarežģīti bet strādā, ļoti nePythonic
# daudz labāk izmantot negatīvo indeksu
print(saraksts[-1]) # pēdējais elements
print(skaitli[-1]) # pēdējais skaitlis

# kā būtu ar priekšpēdējo elementu?
print(saraksts[-2]) # priekšpēdējais elements
print(skaitli[-2]) # priekšpēdējais skaitlis

# vairāk par sarakstime no Google ko tas dod saviem darbiniekiem: https://developers.google.com/edu/python/lists

# tagad apskatīsim vairākku elementu vienlaicīgu piekļuvi
# tam izmantojam "slicing" - sagriešanu 

# piemēram pirmos 4 skaitļus no skaitļu saraksta
print(skaitli[0:4]) # no indeksa 0 līdz 4 (4 nav iekļauts)
# vēl kompaktāk ir bez nulles jo tā ir noklusēta
print(skaitli[:4]) # no sākuma līdz 4 (4 nav iekļauts)

# kā būtu ar pēdejiem 4 skaitļiem?
print(skaitli[-4:]) # no -4 līdz beigām

# es varu salipināt kopā jaunā sarakstā piemēram pirmos 5 un pēdejos 7 skaitļus
jauni_skaitli = skaitli[:5] + skaitli[-7:] # šeit + tiek izmantots divu sarakstu lipināšani iegūstot jaunu sarakstu
print(jauni_skaitli)

# kā būtu ar katru otru skaitli
print(skaitli[::2]) # no sākuma līdz beigām ar soli 2
# kā būtu ar 2 elementu un atkal pa 2
print(skaitli[1::3]) # no indeksa 1 līdz beigām ar soli 3

# liejot : slicing mēs neiegūstam kļūdas var rakstīt arī it kā muļķibas

print(saraksts[-5000:9000]) # ja nav tik daudz elementu, vienkārši atgriež visu kas ir

# kā būtu ar apgrieztu sarakstu? tam var izmanot negatīvu indeksu
aggriezts = skaitli[::-1] # no sākuma līdz beigām ar soli -1
print(aggriezts) # jauns saraksts kas sākas ar 19 un iet uz leju

# mēs mākam pievienot elementus sarakstam ar append
# kā būtu ar dzēšanu?
# izmantojam del atslēgvārdu
del skaitli[1] # dzēšam otro elementu ar indeksu 1
print(skaitli)
# tagad ar indeksu 1 būs skaitlis 2
print(skaitli[1]) # šeit būs 2 jo 1 ir izdzēsts

# ja gribam izdēst teiksim no 5 līdz 7 elementam?
del skaitli[5:8] # dzēšam elementus no indeksa 5 līdz 8 (8 nav iekļauts)
print(skaitli)

# kā būtu ar jauna saraksta pievienošanu beigās
jauni_skaitli = [100, 101, 102]
skaitli += jauni_skaitli # šeit mēs pievienojam jauno sarakstu esošajam sarakstam
# iepriekšējā rindiņa ir līdzīga šādai: skaitli = skaitli + jauni_skaitli
print(skaitli)

# mēs varam arī mainīt kāda elementa vērtību
# mums patlaban elements ar indeksu 4 (5tais elements) ir arī 5
print("Pirms nomaiņas:", skaitli[4])
skaitli[4] = 555 # mainām 5to elementu uz 555, var mainīt uz jebko
print("Pēc nomaiņas:", skaitli[4])
print(skaitli)

# pārbaude vai kāds elements eksistē
# vai Valdis ir sarakstā?
if "Valdis" in saraksts:
    print("Jā, Valdis ir sarakstā.")    
else:
    print("Nē, Valdis nav sarakstā.")

# vai Jānis ir sarakstā?
if "Jānis" in saraksts:
    print("Jā, Jānis ir sarakstā.") 
else:
    print("Nē, Jānis nav sarakstā.")

# jāpiemin ka ļoti lielos sarakstos šāda pārbaude var būt lēna jo Python pārbauda katru elementu pēc kārtas

# atradīsm konkrētu indeksu kādam elementam
# piemēram 16 skaitļu sarakstā
indekss = skaitli.index(16) # atrod indeksa vērtību elementam 16
print(f"Skaitlis 16 ir ar indeksu {indekss}.")

# ja zinam ka var nebūt tad jālieto try except atkal
try:
    indekss = skaitli.index(9999) # mēģinam atrast indeksu elementam 9999
    # ja kļūdas nav tad nākošā rindiņa izpildās, bet ja bija kļūda tad izpildās except bloks
    print(f"Skaitlis 9999 ir ar indeksu {indekss}.")
except ValueError:
    print("Skaitlis 9999 nav sarakstā.")

# Filozofiski runājot saraksti paradzēti homogēniem datiem, bet Python saraksti var saturēt jauktus datus
jaukts_saraksts = ["Oskars", 25, 3.14, True] # vienā sarakstā glaba dažāda tipa datus string, int, float, bool
print(jaukts_saraksts) # tā var, bet tad pazūd dažas priekšrocības

# ja man ir vienāda tipa  dati tad varu darīt dažas ērtas darbības
# piem skaitļiem man ir sum, min, max
print("Mazākais skaitlis", min(skaitli)) # min nestrādātu ar miksētiem ne skaitļu tipiem
print("Lielākais skaitlis", max(skaitli)) # max nestrādātu ar miksētiem ne skaitļu tipiem
print("Skaitļu summa", sum(skaitli)) # sum nestrādātu ar miksētiem ne skaitļu tipiem
# vidēju arī tagad viegli aprēķināt
vidējais = sum(skaitli) / len(skaitli)
print("Skaitļu vidējais:", vidējais)
# noapaļausim līdz 4 zīmēm aiz komata
print("Skaitļu vidējais noapaļots:", round(vidējais, 4))