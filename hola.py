
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
print("numero prar")      
"""
print("numero par")
for nume in range(1,10):
    if nume % 2 == 0:
        print("encontre un # par", nume)
        continue
    print("encontre un numero",nume)
"""
for numero in range(3,30):
    if numero % 2 ==0:
        print("el #: ", numero, "es PAR")
        continue
    print("encontre un numero", numero)

print("serie fibonacci")

####serie fibonacci
def serie_fibonacci(nu):
    "escribe la serie de fibonacci hasta n."
    a,b = 0,1
    while a < nu:
            print(a,end=',')
            ##print(a,end=','+"\n")
            a,b = b, a+b
    print()

serie_fibonacci(2000)
print(serie_fibonacci)
print(serie_fibonacci(0))
####serie fibonacci
###Retornar numeros serie fibonacci
print("otra serie fibonacci")
def fib2(nnn):
    "devuelve una lista conteniendo la serie fibonacci hasta"
    result = []
    a, b = 0, 1
    while a < nnn:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

###otra cosilla
def pedir_confirmacion(prompt, reitentos=4, queja='si o no, por favor'):
    while True:
        ok = input(prompt)
        if  ok in ('s','S','si','Si','SI'):
            return True
        if ok in ('n','no','No','NO'):
            return False
        reintentos = reitentos - 1
        if reintentos < 0:
            raise OSError('usuario duro')
        print(queja)


pedir_confirmacion('realmente quiere salir?')
##pedir_confirmacion('sdfgdf', 2)

        ##pagina 29

        





        





    






