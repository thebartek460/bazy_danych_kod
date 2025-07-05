"""
Moduł: wyszukiwarka.py
Zawiera funkcje do przeszukiwania danych pacjentów i wizyt.
"""

def znajdz_pacjenta_po_peselu(pacjenci, pesel):
    """
    Znajduje pacjenta po numerze PESEL.

    Args:
        pacjenci (list): Lista słowników z danymi pacjentów.
        pesel (str): Numer PESEL do wyszukania.

    Returns:
        dict or None: Słownik z danymi pacjenta lub None.
    """
    return next((p for p in pacjenci if p["pesel"] == pesel), None)

def znajdz_wizyty_po_statusie(wizyty, status):
    """
    Zwraca listę wizyt o podanym statusie.

    Args:
        wizyty (list): Lista słowników wizyt.
        status (str): Status wizyty (np. 'zakończona').

    Returns:
        list: Lista słowników z pasującymi wizytami.
    """
    return [w for w in wizyty if w["status"].lower() == status.lower()]
