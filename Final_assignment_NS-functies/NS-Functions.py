

def standaardtarief(afstandKM):
    'berekent het standaard tarief'
    if afstandKM > 50:                                         #als afstand groter is dan 50
        afstandKM = (15 + (afstandKM * 0.60))
    elif afstandKM <= 0:                                       #als afstand kleiner of gelijk is aan 0
        afstandKM = 0
    else:                                                      #als afstand tussen 0 en 50 inzit
        afstandKM = afstandKM * 0.80
    return (afstandKM)


def ritprijs(leeftijd, weekendrit, afstandKM):
    'berekent de volledige ritprijs aan de hand van "leeftijd, weekendrit, en afstand"'
    standaardtarief(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:                          #als de leeftijd buiten de 12 en 65 valt
        if weekendrit == True:                                   #weekend wel of niet
            ritprijs = (standaardtarief(afstandKM) * 0.65)
        else:
            ritprijs = (standaardtarief(afstandKM) * 0.70)
    else:                                                        #als de leeftijd binnen de 12 en 65 valt
        if weekendrit == True:                                   #weekend wel of niet
            ritprijs = (standaardtarief(afstandKM) * 0.60)
        else:
            ritprijs = (standaardtarief(afstandKM) * 1)
    return ritprijs

#print(ritprijs(leeftijd, weekendrit, afstandKM))

print('prijzen: 11, 12, 35, 64, 65 jaar')
print('wel weekend korte rit')
print(ritprijs(11, True, 10))
print(ritprijs(12, True, 10))
print(ritprijs(35, True, 10))
print(ritprijs(64, True, 10))
print(ritprijs(65, True, 10))
print('geen weekend korte rit')
print(ritprijs(11, False, 10))
print(ritprijs(12, False, 10))
print(ritprijs(35, False, 10))
print(ritprijs(64, False, 10))
print(ritprijs(65, False, 10))
print('wel weekand lange rit')
print(ritprijs(11, True, 100))
print(ritprijs(12, True, 100))
print(ritprijs(35, True, 100))
print(ritprijs(64, True, 100))
print(ritprijs(65, True, 100))
print('geen weekend lange rit')
print(ritprijs(11, False, 100))
print(ritprijs(12, False, 100))
print(ritprijs(35, False, 100))
print(ritprijs(64, False, 100))
print(ritprijs(65, False, 100))

