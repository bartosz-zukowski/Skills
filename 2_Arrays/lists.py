"""
Masz listę odczytów temperatur z czujników (liczby całkowite, mogą być dodatnie i ujemne).
Twoim zadaniem jest znalezienie tej temperatury, która jest najbliższa zeru.
Dane wejściowe: Lista liczb, np.: temperatury = [-10, 5, -2, 12, -3]
"""

def najblizsza_zeru(temperatury):
    return min(temperatury, key=abs) if temperatury else 0

print(najblizsza_zeru([-10, 5, -2, 12, -3]))  # Output: -2

"""
Masz listę imion. Znajdź imię, które byłoby ostatnie w słowniku (alfabetycznie), 
ale... ignorując wielkość liter (czyli a i A traktujemy tak samo).
Dane: names = ["adam", "Zosia", "Beata"]

"""

def ostatnie_imie(names):
    return max(names, key=str.lower) if names else ""

print(ostatnie_imie(["adam", "Zosia", "Beata"]))  # Output: Zosia


"""
Masz listę liczb, ale... one są zapisane jako tekst (stringi). 
Twoim zadaniem jest znalezienie największej liczby (matematycznie).
Dane: liczby = ["5", "9", "12", "100", "3"]
"""

def najwieksza_liczba(liczby):
    if not liczby:
        return None
    return str(max(list(map(int, liczby))))

print(najwieksza_liczba(["5", "9", "12", "100", "3"]))  # Output: 100

def najwieksza_liczba_liner(liczby):
    return max(liczby, key=int) if liczby else None

print(najwieksza_liczba_liner(["5", "9", "12", "100", "3"]))  # Output: 100