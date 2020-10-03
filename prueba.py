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
x=diccionario2.get("2")      ##Metodo para obtener un valor del diccionario a partir de un indice
print(diccionario2)
diccionario2.pop("6")        ##Metodo para eliminar un valor del diccionario a partir del indice
print(diccionario2)








#print(lista1)

#print(lista2)


