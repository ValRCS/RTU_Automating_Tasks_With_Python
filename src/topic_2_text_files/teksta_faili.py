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

# mēs varam lietot arī relatīvo ceļu
# vienkārši rakstīt faila nosaukumu pa tiešo
with open("apraksts.txt", "w", encoding="utf-8") as file:
    file.write("Jauns teksts kas pārraksta iepriekšējo aprakstu.")
    print("Apraksts ir saglabāts failā, izmantojot relatīvo ceļu.")