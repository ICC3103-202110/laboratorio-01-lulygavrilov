lista = []
for i in range(10):
    elemento = []
    for j in range(10):
        elemento.append(i+j)
    lista.append(elemento)

for i in lista:
    print(i)