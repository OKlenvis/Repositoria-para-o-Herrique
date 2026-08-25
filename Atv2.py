O=str(input("Escolh um operador (+, -, * ou /): "))
n1=float(input("Primeiro número: "))
n2=float(input("Sgundo Número: "))


if O == '+':
    print(n1+n2)

elif O == "-":
    print(n1-n2)

elif O == "*":
    print(n1*n2)

else:
    print(n1/n2)

