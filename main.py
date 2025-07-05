from raport import zaladuj_dane, raport_ogolny
from wyszukiwarka import znajdz_pacjenta_po_peselu, znajdz_wizyty_po_statusie

# Ścieżki do plików
sciezka_pacjenci = "patients.csv"
sciezka_lekarze = "doctors.csv"
sciezka_wizyty = "visits.csv"

# Wczytanie danych
pacjenci = zaladuj_dane(sciezka_pacjenci)
lekarze = zaladuj_dane(sciezka_lekarze)
wizyty = zaladuj_dane(sciezka_wizyty)

def menu():
    print("\n=== MENU ===")
    print("1. Raport: liczba wizyt dla każdego lekarza")
    print("2. Wyszukaj pacjenta po numerze PESEL")
    print("3. Znajdź wizyty o statusie")
    print("0. Wyjście")

while True:
    menu()
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        raport_ogolny(wizyty, lekarze)

    elif wybor == "2":
        pesel = input("Podaj numer PESEL pacjenta: ")
        pacjent = znajdz_pacjenta_po_peselu(pacjenci, pesel)
        if pacjent:
            print("\nZnaleziono pacjenta:")
            for k, v in pacjent.items():
                print(f"{k}: {v}")
        else:
            print("Nie znaleziono pacjenta o podanym numerze PESEL.")

    elif wybor == "3":
        status = input("Podaj status wizyty (np. zakończona, odwołana): ")
        wyniki = znajdz_wizyty_po_statusie(wizyty, status)
        print(f"\nZnaleziono {len(wyniki)} wizyt o statusie '{status}':")
        for w in wyniki:
            print(w)

    elif wybor == "0":
        print("Zakończono działanie programu.")
        break

    else:
        print("Nieprawidłowa opcja. Wybierz ponownie.")
