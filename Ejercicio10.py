'''
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla 
cada uno de los productos en una línea distinta.
'''

productos = input("Ingrese su lista de productos, separados por comas: ")

lista_productos = productos.split(',')

for indice_producto in range( len(lista_productos) ):
    print("producto %d:%10s" % (indice_producto, lista_productos[indice_producto]) )
