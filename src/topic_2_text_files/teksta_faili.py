# Tātad šodien strādāsim ar teksta failiem Python valodā.

# vispirms atradīsim kur mēs esam
from pathlib import Path # tā ir standarta bibliotēkas daļa
print(Path.cwd()) # cwd nozīmē "current working directory"
current_dir = Path.cwd() # saglabājam pašreizējo direktoriju mainīgajā
print(f"Pašreizēja mape ir: {current_dir}")
# atceramies f-strings ļauj mums ērti ievietot mainīgos tekstā

# pārbaudīsim vai teksta_faili.py ir tajā pašā mapē
file_path = current_dir / "teksta_faili.py" # veidojam ceļu uz failu
print(f"Faila ceļš ir: {file_path}")
# pārbaudam vai eksistē
if file_path.exists():
    # viens zarojums ja eksistē
    print("Fails eksistē šajā mapē!")
    print("Viss kārtībā, varam turpināt darbu ar failiem.")
else:
    # cits zarojums ja neeksistē
    print("Fails neeksistē šajā mapē!")
    # šis zarojums vēl joprojām ir spēka

# te vairs nav zarojuma, jo esam atgriezušies sākotnējā plūsma

name = "Valdis"
job = "datorspeciālists"
full_description = f"{name} strādā kā {job}."
print(full_description)

# saglabāsim šo aprakstu teksta failā
output_file_path = current_dir / "apraksts.txt" # veidojam ceļu
print(f"Saglabāsim aprakstu failā: {output_file_path}")

# atvērsim jaunu (vai pārrakstīsim esošu) failu rakstīšanas režīmā
# w nozīmē write (rakstīt)
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(full_description) # ierakstām aprakstu failā
    print("Apraksts ir saglabāts failā.")
# tātad šeit man ir jau jauns fails ar aprakstu

# mēs varam lietot arī relatīvo ceļu
# vienkārši rakstīt faila nosaukumu pa tiešo
# tas nozīme ka ceļs ir relatīvs pret patreizējo ceļu, lai kas tas būtu
with open("apraksts.txt", "w", encoding="utf-8") as file:
    file.write("Jauns teksts kas pārraksta iepriekšējo aprakstu.")
    print("Apraksts ir saglabāts failā, izmantojot relatīvo ceļu.")

# taisam 5 min pauzi :) un tad turpinam darbu ar failiem

# apskatīsm kādi *.txt faili ir mūsu  patreizējā mapē
txt_files = list(current_dir.glob("*.txt")) # glob meklē failus pēc parauga
print("Teksta faili šajā mapē ir:")
# ar for cikklu izdrukāsim atrastos failus pa vienam
for txt_file in txt_files:
    print(txt_file.name)
    # izdrukāsim arī pilno ceļu
    print(f"Pilnais ceļš: {txt_file.resolve()}") # absolūtais ceļš

# absolūtais ceļs ir noderīgs, lai precīzi zinātu kur atrodas fails sistēmā

# bet tagad saskaitīsm cik man ir texta failu šajā mapē
# saglabāšu so skaitu mainīgajā
file_count = len(txt_files) # skaitām failu saraksta garumu
print(f"Kopā šajā mapē ir {file_count} teksta faili.")

# saskaitīsm cik man ir .txt failu šajā mapē: D:\Github\RTU_Automating_Tasks_With_Python
# rglob strāda rekursīvi visās apakšmapēs, un apakšmapju apakšmapēs utt
# jauna failu nosaukumu kolekcija kuru saglabājam mainīgajā
# text_files_in_project = list(Path(r"D:\Github\RTU_Automating_Tasks_With_Python").rglob("*.txt"))
# tāpatās var meklēt citus pagarinājumus
# arī var atrast konkrētus failus pēc nosaukuma

# print("Teksta faili projektā ir:")
# for text_file in text_files_in_project: # for ciklā es izmantoju text_file kā pagaidu mainīgo individuāliem failiem
#     print(text_file.resolve()) # izdrukājam pilno ceļu

# # cik ir visā projektā .txt faili?
# total_text_file_count = len(text_files_in_project)
# print(f"Kopā projektā ir {total_text_file_count} teksta faili.")

# mazā mapē - ievērojam ka arī atstarpe mapes nosaukumā ir atbalstīta
text_faili_maza_mape = list(Path(r"D:\Github\RTU_Automating_Tasks_With_Python\src\topic_2_text_files\pārbaudes mape").rglob("*.txt"))
print("Teksta faili mazā mapē ir:")
for text_file in text_faili_maza_mape:
    print(text_file.resolve()) # izdrukājam pilno ceļu

# cik ir mazā mapē .txt faili?
total_text_file_count_maza_mape = len(text_faili_maza_mape)
print(f"Kopā mazā mapē ir {total_text_file_count_maza_mape} teksta faili.")

# pa relatīvo ceļu mēs varam arī kāpties augšup

# apskatīsim cik .py faili ir vienu līmeni augstāk
py_files_one_level_up = list(Path("..").rglob("*.py")) # viens punkts nozīmē pašreizējo mapi, divi punkti - vienu līmeni augstāk
print("Python faili vienu līmeni augstāk ir:")
for py_file in py_files_one_level_up:
    print(py_file.resolve())

# atgriežamies pie teksta failiem:
# izdrukāsim visu sarakstu uzreiz bez cikla
print("Teksta faili kuri ir patreizējā mapē:")
print(txt_files)

# pāriesim pie viena pat faila

# atradīsim teksta failus kuru nosaukumos ir vārds yeats kaut kur
yeats_files = [] # tukšs saraksts
# sarakstus mēs izmantojam lai glabātu potenciāli daudz saistītas informācijas vienuviet
# piemēram failu ceļus, skaitļus, vārdus utt utt
for txt_file in txt_files:
    if "yeats" in txt_file.name.lower(): # pārbaudām vai "yeats" ir faila nosaukumā (mazajiem burtiem)
        yeats_files.append(txt_file) # pievienojam sarakstam atrasto failu
print("Faili ar 'yeats' nosaukumā ir:")
print(yeats_files) # izdrukājam sarakstu ar atrastajiem failiem

# ja mums ir vismaz viens fails tad izdrukāsim tā pilno ceļu
if len(yeats_files) > 0:
    print(f"Pirmais 'yeats' fails ir: {yeats_files[0].resolve()}")
    pirmais_fails = yeats_files[0] # taisu jaunu mainīgo ar pirmo failu sarakstā
else:
    print("Nav atrasts neviens 'yeats' fails. Beidzam darbu")
    # šeit man nav pirmais_fails mainīgā un nav arī idejas ko tur likt
    # iziesim no programmas
    exit() # šis iziet no Python programmas izpildes apstājas

# šinī vietā es zinu ka man eksistē fails ar yeats kaut kur nosaukumā


print("Tagad atvērsim šo failu un izlasīsim tā saturu.")

# te jau beigās arī ir tas pats exit() tikai noklusēts

with open(pirmais_fails, "r", encoding="utf-8") as file:
    file_content = file.read() # nolasām visu faila saturu mainīgajā
    print("Faila saturs ir:")
    # fails te vel ir atvērts
# te jau ciet, bet mēs paspējām nolasīt saturu


print(file_content) # izdrukājam faila saturu

# tikpat labi es varētu atvērt šo failu izmantojot relativo ceļu
# ja es zinu ka fails ir patreizejā mapē
with open("the_choice_yeats.txt", "r", encoding="utf-8") as file:
    file_content_relative = file.read()

# atkal fails ir jau aizvērts

print("Faila saturs, nolasīts ar relatīvo ceļu:")
print(file_content_relative)

# pārbaudīsim vai saturs ir vienāds
if file_content == file_content_relative:
    print("Saturs ir vienāds abos gadījumos.")
else:
    print("Saturs atšķiras!")

# nolasīsim failu bet kā rindiņu sarakstu
with open(pirmais_fails, "r", encoding="utf-8") as file:
    lines = file.readlines() # nolasām visas rindiņas kā sarakstu
# fails jau ciet bet rindiņas mums jau ir

print("Faila rindiņas ir:")
print(lines) # izdrukājam rindiņu sarakstu

# atradīsim visas rindiņas kuras sākas ar lielo A burtu
a_lines = [] # tukšs saraksts, tipiski informācijas glabāšanai
for line in lines: # es eju rindiņam cauri pa vienai
    # nākošo rindiņu var modificēt savām vajadzībām
    if line.startswith("A"): # pārbaudām vai rindiņa sākas ar "A"
        a_lines.append(line) # pievienojam sarakstam    

print("Rindiņas, kas sākas ar 'A':")
print(a_lines) # izdrukājam atrastās rindiņas

# tagad ierakstīsim A rindiņas jaunā failā
with open("a_lines.txt", "w", encoding="utf-8") as file:
    for a_line in a_lines: # ejam cauri atrastajām A rindiņām
        file.write(a_line) # ierakstām katru rindiņu failā
    print("A rindiņas ir saglabātas failā a_lines.txt.")