# Si es multiplo de 3 muestra FISS
# Si es de 5 muestra buss
# si es de ambos fissbuzz
# si no muestra el numero
# pseudo codigo  DESIGN
# Repito numeros del 1 al
# 100 comenzando desde 1 si
# es multiplo de 3
# es decir que el resto debe ser 0
# muestra la FIZZ, Si es multiplo de 5
# y el resto da
# 0 muestra BUZZ, Si es multiplo de ambos
# muestra FIZZBUZZ, Si no es multiplo de
# ninguno muestra el numero """

a = 1
while a <= 100:
    if a % 3 == 0 and a % 5 == 0:
        print "FizzBuzz"
    elif a % 3 == 0:
        print "Fizz"
    elif a % 5 == 0:
        print "Buzz"
    else:
        print a
    a = a + 1
