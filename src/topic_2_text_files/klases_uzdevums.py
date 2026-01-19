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


