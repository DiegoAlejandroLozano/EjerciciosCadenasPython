'''
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de 
letras que tienen el nombre.
'''

nombre = input("\nIngrese su nombre: ")
print("%s tiene %d letras" % (nombre, len(nombre)))