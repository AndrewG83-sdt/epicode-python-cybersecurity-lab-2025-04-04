import math

scelta = input("Scegli figura (quadrato, cerchio, rettangolo): ")

if scelta == "quadrato":
    lato = float(input("Inserisci il lato: "))
    print("Perimetro:", lato * 4)

elif scelta == "cerchio":
    r = float(input("Inserisci il raggio: "))
    print("Circonferenza:", 2 * math.pi * r)

elif scelta == "rettangolo":
    base = float(input("Inserisci la base: "))
    altezza = float(input("Inserisci l'altezza: "))
    print("Perimetro:", 2 * (base + altezza))

else:
    print("Figura non valida.")
