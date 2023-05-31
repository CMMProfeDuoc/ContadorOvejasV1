import os
from os import system

ovejas_color = ["negro","blanco","morado","verde","amarillo","rojo"]
ovejas_precio = [800,1200,3000,2670,1500,3410]
ovejas_contador = [0] * len(ovejas_color)

sel = ""

#insertar ovejas

#contar ovejas
while(True):
    black_sheep = 0
    for i in range(0,10):
        while(True):
            system("cls")
            print("Oveja",i+1,"\n")
            for j in range(len(ovejas_color)):
                print(j+1,ovejas_color[j])
            print("0 Lobo !!! ")

            sel = input(">> ")
            if (sel.isnumeric()):
                if(int(sel) in range(1,len(ovejas_color)+1)):
                    sel = int(sel)-1
                    break
            print("Seleccion no valida") #esto no alcanza ni a imprimirse antes del cls       

        if (sel == 0):
            black_sheep+=1

        if (sel < 0): #LOBO
            break

        ovejas_contador[sel]+=1

    #condiciones para salir
    #1 - Muchas ovejas negras
    if (black_sheep >= 6):
        print("Hay muchas ovejas negras")
        system("pause")
        break
    
    #2 - Mucho mora
    if (ovejas_contador[2] > ovejas_contador[3]):
        print("Muchas ovejas moradas 🐑🐑")
        system("pause")
        break

    #3 - LOBO!!
    if (sel < 0):
        print("LOBOOOOO!!")
        system("pause")
        break
    
    #4 - Muuucho rojo
    if (ovejas_contador[5] > 30):
        print("Mucho rojo")
        system("pause")
        break

    salir = input("Desea seguir contando? <si> <no>")
    if (salir == "no"):
        break

#imprimir ovejas
system("cls")
print("Usted tiene: ")
for i in range(len(ovejas_color)):
    print("oveja(s)",ovejas_color[i],ovejas_contador[i])
system("pause")

#calcular precio
system("cls")
print("Precio total")
ganancia_total = 0
for i in range(len(ovejas_contador)):
    total_oveja = ovejas_precio[i] * ovejas_contador[i]
    ganancia_total += total_oveja
    print("Ganancia Ovejas",ovejas_color[i],": $",total_oveja)
print("\nCon un total de: $",ganancia_total)
system("pause")
system("cls")