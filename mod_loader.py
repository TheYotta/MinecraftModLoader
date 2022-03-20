import os
from colored import fg

while True:
    current_mod = ""
    dirs_cleared = []
    text_f = open('modpacks.txt', "r")
    mods = text_f.read().strip().split(",")
    dirs = os.listdir()
    for dir in dirs:
        a = dir.split(".")
        if len(a) == 1 and dir != "mods":
            dirs_cleared.append(a[0])

    for mod in mods:
        if mod not in dirs_cleared:
            current_mod = mod

    print_mods = mods[:]
    print_mods.remove(current_mod)
    wanted_mod = input(fg("yellow")+f"WANTED MOD (CURRENT - {current_mod} || OPTIONS - {print_mods}):")

    if wanted_mod in dirs_cleared:
        if current_mod != "":
            os.rename("mods", current_mod)
        os.rename(wanted_mod, "mods")
        print(fg("green")+f"LOADED [{wanted_mod}]")
    if wanted_mod not in dirs_cleared:
        print(fg("red")+"THIS MOD ISN'T DEFINED (modpacks.txt)")
