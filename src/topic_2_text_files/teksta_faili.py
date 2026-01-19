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
text_files_in_project = list(Path(r"D:\Github\RTU_Automating_Tasks_With_Python").rglob("*.txt"))
# tāpatās var meklēt citus pagarinājumus
# arī var atrast konkrētus failus pēc nosaukuma

print("Teksta faili projektā ir:")
for text_file in text_files_in_project: # for ciklā es izmantoju text_file kā pagaidu mainīgo individuāliem failiem
    print(text_file.resolve()) # izdrukājam pilno ceļu

# cik ir visā projektā .txt faili?
total_text_file_count = len(text_files_in_project)
print(f"Kopā projektā ir {total_text_file_count} teksta faili.")

# mazā mapē - ievērojam ka arī atstarpe mapes nosaukumā ir atbalstīta
text_faili_maza_mape = list(Path(r"D:\Github\RTU_Automating_Tasks_With_Python\src\topic_2_text_files\pārbaudes mape").rglob("*.txt"))
print("Teksta faili mazā mapē ir:")
for text_file in text_faili_maza_mape:
    print(text_file.resolve()) # izdrukājam pilno ceļu

# cik ir mazā mapē .txt faili?
total_text_file_count_maza_mape = len(text_faili_maza_mape)
print(f"Kopā mazā mapē ir {total_text_file_count_maza_mape} teksta faili.")

