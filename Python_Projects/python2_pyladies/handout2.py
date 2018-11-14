from random import randrange

tahy = ['kamen', 'nuzky', 'papir']
tah_pocitace = tahy[randrange(3)]

tah_cloveka = input("kamen,nuzky nebo papir?")
print('pocitac vybral', tah_pocitace)

if tah_cloveka == tah_pocitace:
    print('stejne hodnoty')

elif tah_cloveka == "kamen" and tah_pocitace =='nuzky':
    print('clovek vyhrava')

elif tah_cloveka == 'kamen' and tah_pocitace =="papir":
    print('pocitac vyhrava')

elif tah_cloveka =='nuzky' and tah_pocitace == 'kamen':
    print('pocitac vyhrava')

elif tah_cloveka == 'nuzky' and tah_pocitace == 'papir':
    print('clovek vyhrava')

elif tah_cloveka == 'papir' and tah_pocitace == 'kamen':
    print('clovek vyhrava')

elif tah_cloveka == 'papir' and tah_pocitace == 'nuzky':
    print('pocitac vyhrava')

else:
    print("invalid input")
    