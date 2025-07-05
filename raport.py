"""
Moduł: raport.py
Zawiera funkcje do raportowania danych z bazy przychodni.
"""

import csv
from collections import Counter

def zaladuj_dane(sciezka_csv):
    """
    Wczytuje dane z pliku CSV do listy słowników.

    Args:
        sciezka_csv (str): Ścieżka do pliku CSV.

    Returns:
        list: Lista rekordów jako słowniki.
    """
    with open(sciezka_csv, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))

def raport_ogolny(wizyty, lekarze):
    """
    Generuje raport podsumowujący liczbę wizyt dla każdego lekarza.

    Args:
        wizyty (list): Lista wizyt.
        lekarze (list): Lista lekarzy.
    """
    lekarz_map = {lekarz['id']: f"{lekarz['first_name']} {lekarz['last_name']}" for lekarz in lekarze}
    licznik = Counter(wizyta['doctor_id'] for wizyta in wizyty)

    print("Liczba wizyt na lekarza:")
    for doc_id, liczba in licznik.items():
        print(f"- {lekarz_map.get(doc_id, 'Nieznany')} ({doc_id}): {liczba} wizyt")
