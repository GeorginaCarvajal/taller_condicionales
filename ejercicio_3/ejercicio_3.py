#Programa para definir las ganancias de los productos de una tienda

print("--------------------------------")
print("-----Ganancias del vendedor-----")
print("--------------------------------")

#input
p_compra=float(input("digite el valor del producto: "))

# processing
if p_compra<3000:
    ganancia=(p-compra*0.15)
    p_venta=p_compra+ganancia
else:
    if p_compra>=3000 and p_compra<=6000:
        ganancia=500
        p_venta=p_compra+ganancia
    else:
        if p_compra>6000:
            ganancia=(p_compra*0.25)
            p_venta=p_compra+ganancia
    
# output
print("--------------------------------")
print("--resultados de las ganancias---")
print("--------------------------------")