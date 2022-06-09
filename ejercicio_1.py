from cgi import print_arguments
from typing import Iterable

"""Habiendo dos listas. Devolver “Parecidas” si hay al menos 2 elementos en
común. En caso contrario devolver “No coinciden”."""

def listas_parecidas():

    lista_uno= (1,2,3,4)
    lista_dos=(5,6,7)

    for x in lista_uno:
        for y in lista_dos:
            if y == x:
                return("Las listas son parecidas")
    
    return("Las listas no coinciden")

print(listas_parecidas())