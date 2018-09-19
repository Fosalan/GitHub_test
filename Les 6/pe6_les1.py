def hello(name):
    'zegt hallo'
    print('hallo, ' + name)


hello('Niels')



def rng(lst):
    x = max(lst) - min(lst)
    return (x)

lijst = [1,2,35,6,]
bereik = rng(lijst)
print('het bereik van ' + str(lijst) + ' is' + str(bereik))

help(hello)