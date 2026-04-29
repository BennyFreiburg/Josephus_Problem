import math

def josephus_problem():
    print("Sie sitzen im Kreis und jeder Zweite wird ausgesiebt.")
    print("Wer am Schluss übrig bleibt gewinnt. Sie suchen den besten Sitzplatz.")
    anzahl = int(input("Geben Sie die Anzahl der Teilnehmer an: "))
    
    a = math.log(anzahl) / math.log(2)
    b = int(math.floor(a))
    sitzplatz = 2 * anzahl - (2 * int(math.pow(2, b)) - 1)
    
    print("Der beste Sitzplatz ist:", sitzplatz)

if __name__ == "__main__":
    josephus_problem()