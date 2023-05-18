print('Se pide obtener los números primos comprendidos entre 1 y 500.')
primos=[]
for num in range(1, 501):
    if num == 1:
        continue
    primo=True
    for i in range(2, num):
        if num%i == 0:
            primo=False
            break
    if primo == True:
        primos.append(num)
print('Los números primos que se obtenieron del rango antes entregado son:',primos)