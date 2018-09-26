
grondgetallen = [4,5,3,-81]

def kwadraten_som(grondgetallen):
    'vind de positieve getallen in een lijst en kwadrateert deze'
    res = 0
    for x in grondgetallen:
        if x > 0:   #als x positief is
            res = (res + x**2)      #kwadrateer x
        else:
            return(res)
    return(res)



print(kwadraten_som(grondgetallen))