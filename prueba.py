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

diccionario={
    "hola": "Caquita seca",
    "holi": "Caquita feliz",
    "holiwi": "Tu mamá es el jaime"
}
x=diccionario.get("holi")
diccionario["holi"]="Mojon contento"
x=diccionario.get("holi")
y=diccionario2["5"]="Caquita"
print(x)
print(diccionario2)




#print(lista1)

#print(lista2)


