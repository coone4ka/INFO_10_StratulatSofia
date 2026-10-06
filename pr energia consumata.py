Putere = int(input("Dati putereea(W): "))
Timp = int(input("Dati timpul(h): "))
Energie = Putere * Timp/ 1000
print(f'Spre achitare : {Energie:.2f} kWh')
Tarif = float(input('Dati tariful actual: '))
Cost = Energie * Tarif
print(f'Spre achitare : {Cost:.2f} lei')
