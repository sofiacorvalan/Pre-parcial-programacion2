"""Realizar un programa para una Facultad donde almacene alumnos con la
siguiente información: nombre, DNI, legajo, hermanos en la escuela (si no se
pasa un parámetro indicando esta información se entiende que el número es 0)
y una lista de materias la cual debe ser completada mediante el método
completar_materias. Este método al principio pedirá la cantidad de materias
a ingresar y luego irá pidiendo al alumno por pantalla una a una las materias.
El legajo se genera de la siguiente manera: ALU_(primeros 3 digitos de DNI). El
método que genere el legajo debe llamarse generar_legajo.
Diseñar otro método que pregunte al alumno la nota que ha sacado en cada
asignatura y elimine de la lista las asignaturas aprobadas. Al final el método
debe mostrar por pantalla las asignaturas que el alumno tiene pendiente. Este
método debe llamarse registrar_notas.
Ayuda: remove() es una funcion que elimina elementros de una lista.
Nota: Una asignatura se aprueba con una nota igual o mayor a 6."""

class Alumnos():
    def __init__(self, nombre, dni,legajo,hermanos):
        self.nombre=nombre
        self.dni=dni
        self.legajo= self.generar_legajo()
        self.hermanos=hermanos
        self.materias=self.completar_materias()
    
    def generar_legajo():
        pass

    def completar_materias(self, cantidad_materias):
        self.cantidad_materias= int (input("Ingrese la cantidad de materias: "))

        for x in cantidad_materias:
            print("¿La materia numero", x, "esta aprobada?")
            aprobada=input("Reponda con si o no:")
            lista_mat: int

            if aprobada == "si":
                lista_mat=lista_mat+1

        return lista_mat
