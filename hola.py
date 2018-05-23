
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
    if len(p) > 6:
        palabras.insert(0,6)

palabras






