print('Hola mundo')
x=5
y=9
i=0
suma=x+y
print(suma)
lista2=[]
lista1=[]
lista3=[]
for i in range(4):
    lista1.append(i)

for i in lista1:
    print(lista1[i])
for i in lista1:
    x=int(input("Ingrese numero para la lista: "))
    lista2.append(x)


lista1.sort()
lista2.sort()
lista3=[lista1,lista2]


print(lista1)
print(lista2)
print(lista3)
type(lista3)

