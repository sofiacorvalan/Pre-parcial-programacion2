"""Escribir un programa que cree un diccionario vacío y se vaya llenando con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un
nuevo dato debe imprimirse el contenido del diccionario. Tener en cuenta que
no siempre se piden los mismos datos a todos."""

persona = {}

nombre = {"nombre": input("Ingrese su nombre: ")}
persona.update(nombre)
print (persona.items())

edad = {"edad": input("Ingrese su edad: ")}
persona.update(edad)
print (persona.items())

sexo = {"sexo": input("Ingrese su sexo: ")}
persona.update(sexo)
print (persona.items())

telefono = {"telefono": input("Ingrese su numero de telefono: ")}
persona.update(telefono)
print (persona.items())




