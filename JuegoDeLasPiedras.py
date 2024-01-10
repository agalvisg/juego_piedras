
import random

def GameOfStones():
    
    numero_piedras=random.randint(10,30)
    print(f"El número de inicial de piedras es: {numero_piedras}")
    
    while True:
        eleccion=random.choice([2,3,5])
        print(f"P1 eligió {eleccion}")
        numero_piedras-=eleccion
        print(f"Quedan {numero_piedras} piedras")
        
        if numero_piedras<=0:
            print("P2 gana")
            break
        
        eleccion=0
        if numero_piedras % 7 == 0 or numero_piedras % 8 == 0:
            print("P1 gana")
            break
        else:
            if (numero_piedras-2) % 7 == 0 or (numero_piedras-2) % 8 == 0:
                eleccion=2
            elif (numero_piedras-3) % 7 == 0 or (numero_piedras-3) % 8 == 0:
                eleccion=3
            elif (numero_piedras-5) % 7 == 0 or (numero_piedras-5) % 8 == 0:
                eleccion=5
            else:
                eleccion = random.choice ([2,3,5])
            
            print (f"P2 eligió {eleccion}")
            numero_piedras-=eleccion
            print(f"Quedan {numero_piedras} piedras.")
            
            if numero_piedras <= 0:
                print ("P1 gana")
                break
            
GameOfStones()