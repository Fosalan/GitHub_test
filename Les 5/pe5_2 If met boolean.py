age = eval(input('Geef je leeftijd:'))
nationality = input('Heb je een Nederlands paspoort (ja/nee):')
if age >= 18 and nationality == 'ja':
    print('Gefeliciteerd, je mag stemmen')
else:
    print('Je mag niet stemmen')