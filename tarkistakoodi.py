import sys

# Luetaan tiedosto rivi riviltä
try:
    with open('koodi.txt', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if "TODO" in line:
                print(f"VIRHE rivillä {i+1}: TODO löydetty!")
                sys.exit(1) # Punainen valo CI-putkessa

    print("Koodi puhdas.")
    sys.exit(0) # Vihreä valo
except FileNotFoundError:
    print("Tiedostoa koodi.txt ei löytynyt.")
