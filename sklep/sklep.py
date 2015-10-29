#buty = {'klapki':15, 'sandaly':20, 'trampki':25, 'kalosze':30, 'chodaki':20, 'kapcie':15, 'kozaki':45}

fhand = open('buty.txt','r')
for line in fhand:
        line = line.rstrip()
        print line
        
counts = dict()
print 'Wpisz nazwe towaru, ktory chcesz wlozyc do koszyka. Jesli skonczyles zakupy wpisz: "koniec"'

while True:
        towar = raw_input('Wloz do koszyka: ')
        if towar == 'klapki':
                counts['klapki'] = 15
        elif towar == 'sandaly':
                counts['sandaly'] = 20
        elif towar == 'trampki':
                counts['trampki'] = 25
        elif towar == 'kalosze':
                counts['kalosze'] = 30	
        elif towar == 'chodaki':
                counts['chodaki'] = 20
        elif towar == 'kapcie':
                counts['kapcie'] = 15
        elif towar == 'kozaki':
                counts['kozaki'] = 45	
        elif towar == 'koniec': break
        else:
                print 'Brak tych butow w sprzedazy'

if len(counts.values()) == 0:
        counts['brak'] = 0

bigword = None
bigcount = None
smallword = None
smallcount = None
for word, count in counts.items():
        if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count
                
for word, count in counts.items():                
        if smallcount is None or count < smallcount:
                smallword = word
                smallcount = count
        

def koszyk():
    for key in counts:
        print key, counts[key]

def razem():
    if sum(counts.values()) > 0:
        return sum(counts.values())
    else:
        return '0'
    
def srednia():
    if sum(counts.values())/len(counts.values()) > 0:
        return sum(counts.values())/len(counts.values())
    else:
        return '0'
                
print '\nWybrales nastepujace towary: '
koszyk()
print 'Razem: ', razem(), 'zl\n'
print 'Najdrozsze w koszyku: ', bigword, bigcount, 'zl'
print 'Najtansze w koszyku: ', smallword, smallcount, 'zl\n'
print 'Srednia cena towaru w twoim koszyku: ', srednia(), 'zl\n'




