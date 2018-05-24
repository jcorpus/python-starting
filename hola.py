
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




    






