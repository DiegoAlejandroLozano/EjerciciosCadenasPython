'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el 
programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''

fecha = input("\nIngrese la fecha de nacimiento (dd/mm/aaaa): ")
fecha_dividida = fecha.split('/')
print("Día: %s\nMes: %s\nAño: %s\n" % (fecha_dividida[0], fecha_dividida[1], fecha_dividida[2]))