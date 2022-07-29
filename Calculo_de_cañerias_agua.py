#Definicion de valores
PresEmp = float(input("Elija su presion inicial "))
Altura = float(input("Elija su altura de tanque "))
PresDis = PresEmp - Altura
Gasto = float(input("Cuanto gasto tiene? "))

#Seleccion de diametro
if PresDis <= 4:
    if Gasto <= 0.24 :
        print("Tu sección es de 0.013")
    elif Gasto <= 0.52 :
            print("Tu sección es de 0.019")
    else :
        if Gasto <= 1.06 :
            print("Tu sección es de 0.025")
