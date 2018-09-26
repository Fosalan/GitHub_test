def wijzig(letterlijst):
    'leegt de lijst en voegt d,e,f toe in de lijst'
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')
    return(letterlijst)

lijst = ['a','b','c']
print(lijst)
wijzig(lijst)
print(lijst)