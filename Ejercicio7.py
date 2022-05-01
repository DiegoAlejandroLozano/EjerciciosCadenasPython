'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''

correo = input("\nIngrese su correo: ")
nuevo_correo = correo.split('@')[0] + "@ceu.es"

print("El nuevo correo es: " + nuevo_correo)


