"Programa para determinar si un numero es par o impar"

print("""----------------------------------""")
print("""numero par o impar----------------""")
print("""----------------------------------""")

#input 

x= int(input("Digite un numero"))


#processing

if x % 2 == 0:
    print("El numero es par")

else:
    print("El numero es impar")

#output

print(" El numero es:" + str(x))   

