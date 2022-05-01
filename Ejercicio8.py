'''
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por 
pantalla el número de euros y el número de céntimos del precio introducido.
'''

precio = input("\nPrecio del producto en euros (xxx,xx): ")
print("Número de euros: %s\nNúmero de céntimos: %s\n" % (precio[:precio.find(',')], precio[precio.find(',')+1:]))