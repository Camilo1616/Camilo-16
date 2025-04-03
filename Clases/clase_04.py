#codificacion camel case
# 1.5 FLOAT 35 INT jhoan manuel STR
ventasTotales = 0.0

# solicitar el numero de productos 
numProductos = int(input('ingrese el numero de productos a gestionar: '))

# listas para almacenar la informacion 
nombres = []
precios = []
cantidades = []

print ('ingreso inicial de productos de tienda')
for i in range(numProductos):
    print (f'Producto {i+1}')
    nombre = input('ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('ingrese el precio del producto: '))
    precios.append(precio)
    cantidade = int(input('ingrese la cantidad del producto: '))
    cantidades.append(cantidade)

# ciclo principal menu  
while True: 
    print ('\n --- MENU DE GESTION DROGERIA --- ')
    print ('1. vender producto')
    print ('2. mostrar inventario')
    print ('3. mostrar vendas totales')
    print ('4. salir del programa')

    opcion = int(input("ingrese una opcion del menu del 1 a 4: "))      
    
    if opcion == 1:
        print ('\n vender producto')
        nombreVenta = input('ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('ingrese la cantidad a vender: '))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres [i] == nombreVenta: 
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print (f'venta realizada por un valor de $ {totalVenta:.2f}')
                    print (f'quedan {cantidades[i]} unidades de {nombres[i]} en el inventario')
                else:
                    print (f'no hay suficientes unidades en el inventario ya que tenemos solo {cantidades[i]} unidades')
                break
        if not productoEncontrado:
            print (f'producto {nombreVenta} no encontrado en el inventario')
    
    elif opcion == 2:
        print ('\n inventario de productos')
        for i in range(len(nombres)):
            print (f'productos {i+1}: {nombres[i].capitalize()}, precio: $ {precios[i]:.2f}, cantidad: {cantidades[i]} unidades') 
    elif opcion == 3:
        print (f'las ventas totales son de $ {ventasTotales:.2f}')   
    elif opcion == 4:    
        print ('gracias por usar el programa')
        break
    else: 
        print ('opcion no valida, intente de nuevo')