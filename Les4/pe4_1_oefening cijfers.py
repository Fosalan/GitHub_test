CijferICOR = 7
CijferPROG = 7
CijferCSN = 8
print('CijferICOR:')
print(CijferICOR)
print('CijferPROG:')
print(CijferPROG)
print('CijferCSN:')
print(CijferCSN)

print()

print('gemiddelde:')
Gemiddelde = ((CijferICOR + CijferPROG + CijferCSN)/3)
print(Gemiddelde)

print()

print('Gestelde Beloning hiervoor:')
Beloning = ((CijferICOR + CijferCSN + CijferPROG)*30)
print(Beloning)

print()

Overzicht= 'Mijn cijfers:(gemiddeld een ' + str(Gemiddelde) + ') en leveren een beloning van:' + str(Beloning) + ' op!'

print(Overzicht)


