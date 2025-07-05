"""
Moduł: raport.py
Zawiera funkcje do wczytywania danych i tworzenia raportów.
"""

import csv
from collections import Counter

def zaladuj_dane(sciezka_csv):
    """
    Wczytuje dane z pliku CSV do listy słowników.

    Args:
        sciezka_csv (str): Ścieżka do pliku CSV.

    Returns:
        list: Lista słowników reprezentujących rekordy.
    """
    with open(sciezka_csv, newline='', encoding='utf-8') as plik:
        return list(csv.DictReader(plik))

def raport_ogolny(wizyty, lekarze):
    """
    Wyświetla liczbę wizyt przypisanych do każdego lekarza.

    Args:
        wizyty (list): Lista słowników wizyt.
        lekarze (list): Lista słowników lekarzy.
    """
    map_lekarzy = {l["id"]: f'{l["first_name"]} {l["last_name"]}' for l in lekarze}
    licznik = Counter(w["doctor_id"] for w in wizyty)

    print("\n=== Liczba wizyt dla każdego lekarza ===")
    for id_lekarza, liczba in licznik.items():
        nazwisko = map_lekarzy.get(id_lekarza, "Nieznany lekarz")
        print(f"- {nazwisko} ({id_lekarza}): {liczba} wizyt")
