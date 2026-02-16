import sys

# Luetaan tiedosto rivi riviltä
try:
    with open('esimerkkikoodia.py', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if ("print" in line) or (len(line) > 80):
                print(f"VIRHE rivillä {i+1}: print löydetty tai rivi on yli 80 merkkiä!")
                sys.exit(1)  # Punainen valo CI-putkessa

    print("Koodi puhdas.")
    sys.exit(0)  # Vihreä valo
except FileNotFoundError:
    print("Tiedostoa esimerkkikoodia.py ei löytynyt.")
    sys.exit(1)
