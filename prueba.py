i=0

Tupla=(1,2,3,4,"Holi")  
ListadeTupla= list(Tupla)
ListadeTupla.append(69)
print(ListadeTupla)

Lista=[]
for i in ListadeTupla:
    Lista.append(i)


largo=len(ListadeTupla)
print(largo)

diccionario2={
    "1":"Ramiro",
    "2":"Ricardo",
    "3":"María",
    "4":"Rivaldo"
}


diccionario2["5"]="Nacho"
diccionario2["6"]="Claudio"
copiadiccionario=diccionario2.copy()    ##Metodo para copiar un diccionario
x=diccionario2.get("2")      ##Metodo para obtener un valor del diccionario a partir de un indice
print(diccionario2)
diccionario2.pop("6")        ##Metodo para eliminar un valor del diccionario a partir del indice
del diccionario2["4"]         ##Metodo para eliminar un valor del diccionario a partir del indice
diccionario2.popitem()       ##Metodo para eliminar el ultimo valor del diccionario
print(diccionario2)
print(copiadiccionario)
diccionario2.clear()         ##Metodo para eliminar todo el contenido del diccionario
print(diccionario2)








#print(lista1)

#print(lista2)


