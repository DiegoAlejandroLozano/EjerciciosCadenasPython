'''
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y 
la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este 
formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''

numero_telefónico = input("Ingrese el número telefónico (xx-xxxxxxxxx-xx): ")
num_tele_lista = numero_telefónico.split('-')
print("Número de teléfono sin prefijo y sin la extensión: " + num_tele_lista[1])