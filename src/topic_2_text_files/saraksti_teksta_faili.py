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