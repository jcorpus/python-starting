
from __future__ import print_function
import sys

def main():
    print ('hola aqui', sys.argv[1])
    
if __name__ == '__main__':
    main()


###### serie fibonacci

a,b = 0,1
while (b<100):
    print( b, end=",")
    a,b = b,a+b


####### sentencia if
print("\n")

x = int(input("ingresa un numero: "))
if x < 0:
    x = 0
    print("negativo cambiado a cero")
elif x == 0:
    print("cero")
elif x == 1:
    print("simple")
else:
    print("mas")

#### sentencia for

palabras = ['gato','julio','skyrim','battlefield3']
for p in palabras:
    print(p, len(p))


### otro for
for a in palabras[:]:
    if len(a) > 6:
        palabras.insert(0,a)
        print(palabras)


print("el # de palabras es: ",len(a),"\n")

##funcion integrada range
print("funcion range")
for p in range(6):
    print(p)

print("---.---")
##range # inicial y final y de cuanto en cuanto salta "3"
for i in range(2,7,3):
    print(i)

###raiz cuadrada
print("\nraiz cuadrada")
lista = []
for num in range(1,11):
    listas = num ** 2
    lista.append(listas)

print(lista)

##iterar indices de una secuencia
print("otro ejemplo")
mnombre = ['julio','cesar','corpus','mechato']
for pe in range(len(mnombre)):
    print(pe,mnombre[pe])

##funcion list
print("funcion list")
print(list(range(5)))

##numeros primos
print("numeros primos")
for nn in range(2, 10):
    for xx in range(2, nn):
        if nn % xx ==0:
            print(nn, 'es igual a', xx, 'X',nn/xx)
            break
    else:
        print(nn, 'es un numero primo')

##numero par        
print("numero par")
for nume in range(1,10):
    if nume % 2 == 0:
        print("encontre un # par", nume)
        continue
    print("encontre un numero",nume)





    






