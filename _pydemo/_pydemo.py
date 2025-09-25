"""
Author: Max Mustermann
Klasse: 4CN, HTL Rennweg

Modul-Dokumentation -- Ähnlich zu JavaDoc. 
Wird angezeigt z.B. mit help(__name__)

Dieses Modul beinhaltet Funktionen zur Berechnung der Fläche und der 
Diagonale eines Rechtecks.

Beispiel:
>>> berechne_flaeche(2, 3)
6
"""

# Metadaten zu dieser Datei:+
__author__ = "Max Mustermann"
__example__ = "SEW4/01/B"  # Gegenstand/Übungsblatt/Aufgabe(Kapitel)
__date__ = "04.09.2025"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import math
import doctest


def berechne_flaeche(breite: float, hoehe: float) -> float:
    """
    Berechnet die Fläche eines Rechtecks.

    Args:
        breite (float): Die Breite des Rechtecks.
        hoehe (float): Die Höhe des Rechtecks.

    Returns:
        float: Die berechnete Fläche.

    Examples:
        >>> berechne_flaeche(5, 10)
        50
        >>> berechne_flaeche(0, 10)
        0
    """
    return breite * hoehe


def berechne_diagonale(breite: float, hoehe: float) -> float:
    """
    Berechnet die Länge der Diagonale eines Rechtecks
    mithilfe des Satzes von Pythagoras.

    Args:
        breite (float): Die Breite des Rechtecks.
        hoehe (float): Die Höhe des Rechtecks.

    Returns:
        float: Die Länge der Diagonale.

    Examples:
        >>> berechne_diagonale(3, 4)
        5.0
        >>> round(berechne_diagonale(5, 12), 2)
        13.0
        >>> round(berechne_diagonale(1, 1), 2)
        1.41
        """
    return math.sqrt(breite ** 2 + hoehe ** 2)


def main() -> None:
    """
    Hauptfunktion des Programms.
    Fragt den Benutzer nach Breite und Höhe und gibt Fläche und Diagonale aus.
    Führt außerdem die Doctests aus.
    """
    doctest.testmod()

    try:  # Bei einem ungültigen Zeichen beim Umwandeln eines Strings in ein float -> Exception abfangen!
        breite: float = float(input("Gib die Breite des Rechtecks ein (in cm): "))
        hoehe: float = float(input("Gib die Höhe des Rechtecks ein (in cm): "))

        flaeche: float = berechne_flaeche(breite, hoehe)
        diagonale: float = berechne_diagonale(breite, hoehe)

        print(f"Die Fläche beträgt {flaeche:.2f} cm².")
        print(f"Die Diagonale beträgt {diagonale:.2f} cm.")
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine Zahl ein.")


if __name__ == "__main__":
    main()
