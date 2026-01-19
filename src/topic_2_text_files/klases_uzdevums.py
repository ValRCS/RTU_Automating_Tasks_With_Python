# Atvērt veidenbaums.txt
# Nolasit visu saturu rindās (kā list)
# Izveidot jaunu sarakstu ar []
# iet cauri satura sarakstam
# ja rinda ir dzeja tad to pielipinam jaunajam sarakstam  ar append
# kas ir dzeja divi nosacījumi
# ir vismaz kaut kas tātad pēc rinda.strip() garums ar len būs > 0
# otrs nosacījums: rinda nesatur ***

# saglabājam jauno sarakstu jaunā failā ar writelines

# par strip

dirty_city = "      Rīga \n\n \t    "
clean_city = dirty_city.strip() # noņem arī jaunās rindas
print(dirty_city)
print(clean_city)

rinda_ar_whitespace = "   \n    \t \n"
print(f"Pirms strip: '{rinda_ar_whitespace}'")
# garums
print(f"Garums pirms strip: {len(rinda_ar_whitespace)}")
# noņemam whitespace
tira_rinda = rinda_ar_whitespace.strip()
print(f"Pēc strip: '{tira_rinda}'")
print(f"Garums pēc strip: {len(tira_rinda)}")

# tātad var pārbaudīt vai rinda ir tukša ar šadu nosacījumu
if len(rinda_ar_whitespace.strip()) > 0:
    print("Rinda nav tukša")
else:
    print("Rinda ir tukša")

# savukārt vai rindā ir 3 zvaigznītes var pārbaudīt ar in operatoru
rinda = "Šī ir rinda ar *** zvaigznītēm"
if "***" in rinda:
    print("Rindā ir zvaigznītes")
else:
    print("Rindā nav zvaigznītes")

# kā kombinet abus nosacījumus?

rinda = "   ***   "
if len(rinda.strip()) > 0 and "***" not in rinda:
    print("Rinda ir dzeja")
else:
    print("Rinda nav dzeja")

# jums atliekt tātad atvērt veidenbaums.txt failu
# nolasīt saturu kā rindiņu sarakstu
# izveidot jaunu tukšu sarakstu
# iet cauri nolasītajam saturam
# ja rinda ir dzeja (nav tukša un nesatur ***) tad pievienot to jaunajam sarakstam

# 1. solis viens nolasam veidenbaums.txt

# noklusētais režīms ir r - tātad lasīšanas
with open("veidenbaums.txt", encoding="utf-8") as file:
    all_rows = file.readlines() # ielasa visu atmiņā kā rindiņu sarakstu - ja ļoti liels fails tad neder
    # fails vēl te vaļā
# te jau fails ciet

# jauns tukšs saraksts
clean_rows = []

# izejam cauri ar for ciklu visām oriģinām rindām un atsijājam vajadzīgās

for row in all_rows: # iesim cauri visām rindiņām pa vienai
    # šeit mums būs viena rindiņa, kāda nezinam, bet visas apstrādāsim secīgi
    if len(row.strip()) > 0 and "***" not in row:
        clean_rows.append(row) # append modificē clean_rows un pieliek row klāt kā jaunu elementu

# cik oriģināla rindu
print(f"Man ir {len(all_rows)} rindas pirmavota")
# uzrakstīsim cik tad man ir tās tīrās dzejas rindas
print(f"Man ir {len(clean_rows)} rindas dzeju")

# atliek vien saglābat visu tīro jauna failā

# sauksim to par tīro dzeju
with open("veidenbaums_clean.txt", mode="w", encoding="utf-8") as file: # file is a new stream out
    file.writelines(clean_rows)
    # fails vēl te vaļā
# te jau fails ciet
print(f"Tīrā dzeja saglabāta failā veidenbaums_clean.txt.")


# for large text files we can optimize this to open two files at once
# vispirms atveram failu lasīšanai
with open("veidenbaums.txt", encoding="utf-8") as infile:
    # tad atveram jaunu failu rakstīšanai
    with open("veidenbaums_clean_optimized.txt", mode="w", encoding="utf-8") as outfile:
        # te ir abi faili atvērti
        # ejam cauri katrai rindiņai no ieejas faila
        for line in infile: # mēs tātad "dzenam" uz priekšu mūsu izejas failu pa vienai rindiņai
            # pārbaudām vai rinda ir dzeja - te var mainīt loģiku kā gribat
            if len(line.strip()) > 0 and "***" not in line:
                # ja ir dzeja, ierakstām to izejas failā
                outfile.write(line)
        # izejas fails vēl te vaļā
    # ieejas fails vēl te vaļā

# te visi faili ir jau ciet

print("Tīrā dzeja saglabāta failā veidenbaums_clean_optimized.txt.")
