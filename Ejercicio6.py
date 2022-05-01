'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre 
por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

frase = input("\nIntroduzca una frase: ")
vocal = input("Introduzca una vocal: ")

frase_nueva = frase.replace(vocal, vocal.upper())

print("LA FRASE NUEVA ES: " + frase_nueva + "\n")