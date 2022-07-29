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
    else :
        if Gasto <= 1.06 :
            print("Tu sección es de 0.025")
