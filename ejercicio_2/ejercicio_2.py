#Programa que permita realizar un préstamo bancario

print("------------------------------------------------")
print("---Programa para otorgar un prestamo bancario---")
print("------------------------------------------------")

#input
ing = int(input("Digite los ing: "))
deuda = int(input("Digite la deuda: "))

# processing
if ing > 945200:
    if deuda == 0:
        msj = ("Prestamo Aprobado")
    else:
        msj = ("Prestamo No Aprobado")
else:
        msj = ("Prestamo No Aprobado")

# output
print (msj)