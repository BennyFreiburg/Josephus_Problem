def josephus_problem():
    print("Sie sitzen im Kreis und jeder Zweite wird ausgesiebt.")
    print("Wer am Schluss übrig bleibt, gewinnt. Sie suchen den besten Sitzplatz.")
    anzahl = int(input("Geben Sie die Anzahl der Teilnehmer an: "))

    # Berechnung des größten Zweierpotenz kleiner oder gleich anzahl
    potenz = 1 << (anzahl.bit_length() - 1)
    sitzplatz = 2 * (anzahl - potenz) + 1

    print("Der beste Sitzplatz ist:", sitzplatz)

if __name__ == "__main__":
    josephus_problem()