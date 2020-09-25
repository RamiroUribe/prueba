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

diccionario={
    "hola": "Caquita seca",
    "holi": "Caquita feliz",
    "holiwi": "Tu mamá es el jaime"
}
x=diccionario.get("holi")
diccionario["holi"]="Mojon contento"
x=diccionario.get("holi")
print(x)



#print(lista1)

#print(lista2)


