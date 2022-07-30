#Calculo presion disponible
PresEmp = float(input("Elija su presion inicial "))
Altura = float(input("Elija su altura de tanque "))
PresDis = PresEmp - Altura

#Calculo Gasto
RTD = float(input("Capacidad total del TR "))
TempRec = float(input("Indique el tiempo de carga (Seg) "))
Gasto = RTD / TempRec

#Seleccion de diametro
if PresDis <= 4:
    if Gasto <= 0.24 :
        print("Tu sección es de 0.013")
    elif Gasto <= 0.52 :
            print("Tu sección es de 0.019")
    elif Gasto <= 1.06 :
            print("Tu sección es de 0.025")
    elif Gasto <= 1.80 :
            print("Tu sección es de 0.032")
    elif Gasto <= 2.84 :
            print("Tu sección es de 0.038")
    elif Gasto <= 5.08 :
            print("Tu sección es de 0.050")
    elif Gasto <= 7.85 :
            print("Tu sección es de 0.060")
    else :
        if Gasto <= 10.39 :
            print("Tu sección es de 0.075")

elif PresDis == 5 :
    if Gasto <= 0.28 :
        print("Tu sección es de 0.013")
    elif Gasto <= 0.60 :
            print("Tu sección es de 0.019")
    elif Gasto <= 1.18 :
            print("Tu sección es de 0.025")
    elif Gasto <= 2.02 :
            print("Tu sección es de 0.032")
    elif Gasto <= 3.19 :
            print("Tu sección es de 0.038")
    elif Gasto <= 5.70 :
            print("Tu sección es de 0.050")
    elif Gasto <= 8.81 :
            print("Tu sección es de 0.060")
    else :
        if Gasto <= 11.65 :
            print("Tu sección es de 0.075")

elif PresDis == 6 :
    if Gasto <= 0.33 :
        print("Tu sección es de 0.013")
    elif Gasto <= 0.66 :
            print("Tu sección es de 0.019")
    elif Gasto <= 1.30 :
            print("Tu sección es de 0.025")
    elif Gasto <= 2.22 :
            print("Tu sección es de 0.032")
    elif Gasto <= 3.51 :
            print("Tu sección es de 0.038")
    elif Gasto <= 56.26 :
            print("Tu sección es de 0.050")
    elif Gasto <= 9.68 :
            print("Tu sección es de 0.060")
    else :
        if Gasto <= 12.81 :
            print("Tu sección es de 0.075")

elif PresDis == 7 :
    if Gasto <= 0.35 :
        print("Tu sección es de 0.013")
    elif Gasto <= 0.72 :
            print("Tu sección es de 0.019")
    elif Gasto <= 1.41 :
            print("Tu sección es de 0.025")
    elif Gasto <= 2.40 :
            print("Tu sección es de 0.032")
    elif Gasto <= 3.79 :
            print("Tu sección es de 0.038")
    elif Gasto <= 6.77 :
            print("Tu sección es de 0.050")
    elif Gasto <= 10.46 :
            print("Tu sección es de 0.060")
    else :
        if Gasto <= 13.85 :
            print("Tu sección es de 0.075")

elif PresDis == 8 :
    if Gasto <= 0.35 :
        print("Tu sección es de 0.013")
    elif Gasto <= 0.72 :
            print("Tu sección es de 0.019")
    elif Gasto <= 1.41 :
            print("Tu sección es de 0.025")
    elif Gasto <= 2.40 :
            print("Tu sección es de 0.032")
    elif Gasto <= 3.79 :
            print("Tu sección es de 0.038")
    elif Gasto <= 6.77 :
            print("Tu sección es de 0.050")
    elif Gasto <= 10.46 :
            print("Tu sección es de 0.060")
    else :
        if Gasto <= 13.85 :
            print("Tu sección es de 0.075")
