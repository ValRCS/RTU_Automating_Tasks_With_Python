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
    print("Fails eksistē šajā mapē!")
    print("Viss kārtībā, varam turpināt darbu ar failiem.")
else:
    print("Fails neeksistē šajā mapē!")