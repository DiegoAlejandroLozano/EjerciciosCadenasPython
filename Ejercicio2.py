'''
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el 
nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y 
otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''

from matplotlib.pyplot import title


nombre_completo = input("Ingrese su nombre completo: ")

nombre_minusculas = nombre_completo.lower()
nombre_mayusculas = nombre_completo.upper()

letras_mayusculas = ""

for palabra in nombre_completo.split():
    for indice_letra in range(len(palabra)):
        if indice_letra == 0:
            letras_mayusculas += palabra[indice_letra].upper()
        else:
            letras_mayusculas += palabra[indice_letra].lower()

    letras_mayusculas += " "        

print("Nombre es minusculas: " + nombre_minusculas)
print("Nombre es mayusculas: " + nombre_mayusculas)
print("Primera letra en mayúscula: " + letras_mayusculas)
