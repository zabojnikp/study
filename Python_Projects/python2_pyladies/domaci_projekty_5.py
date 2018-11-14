import random

tah_cloveka = ""
tahy = ['kamen', 'nuzky', 'papir']
tah_pocitace = random.choice(tahy)

while tah_cloveka != "konec":
    tah_cloveka = input("kamen,nuzky nebo papir?")

    if tah_cloveka == tah_pocitace:
        print('pocitac vybral', tah_pocitace)
        print('stejne hodnoty')
        
    elif tah_cloveka == "kamen" and tah_pocitace =='nuzky':
        print('pocitac vybral', tah_pocitace)
        print('clovek vyhrava')
                
    elif tah_cloveka == 'kamen' and tah_pocitace =="papir":
        print('pocitac vybral', tah_pocitace)
        print('pocitac vyhrava')
                
    elif tah_cloveka =='nuzky' and tah_pocitace == 'kamen':
        print('pocitac vybral', tah_pocitace)
        print('pocitac vyhrava')
                
    elif tah_cloveka == 'nuzky' and tah_pocitace == 'papir':
        print('pocitac vybral', tah_pocitace)
        print('clovek vyhrava')
        
    elif tah_cloveka == 'papir' and tah_pocitace == 'kamen':
        print('pocitac vybral', tah_pocitace)
        print('clovek vyhrava')
        
    elif tah_cloveka == 'papir' and tah_pocitace == 'nuzky':
        print('pocitac vybral', tah_pocitace)
        print('pocitac vyhrava')
    
    elif tah_cloveka != "konec":
        print("invalid input")

if tah_cloveka == "konec":
    print("game over")