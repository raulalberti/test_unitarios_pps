# Ejercicio para realizar test unitarios
# Calculadora

#Suma
def Suma(x, y):
    if not isinstance(x, (int)) or not isinstance(y, (int)):
        raise ValueError('Los datos deben de ser números enteros')
    return x + y

# Resta
def Resta(x, y):
    return x - y

# Multiplica
def Multiplicar(x, y):
    return x * y

# División
def Dividir(x, y):
    return x / y

# División
def Exponente(x, y):
    return x ** y

#Menu
print(f'-----------------------------------------------')
print(f'Operación a Realizar …….')
print(f'1.Suma')
print(f'2.Resta')
print(f'3.Multiplicar')
print(f'4.Dividir')
print(f'5.Exponente')

# Operación a realizar
choice = input(f'Elige tu operación (1/2/3/4/5):')
print(f'-----------------------------------------------')
dato1 = int(input('Primer dato: '))
dato2 = int(input('Segundo dato: '))
if choice == '1':
    print(dato1, '+', dato2, '=', Suma(dato1, dato2))
elif choice == '2':
    print(dato1, '-', dato2, '=', Resta(dato1, dato2))
elif choice == '3':
    print(dato1, 'x', dato2, '=', Multiplicar(dato1, dato2))
elif choice == '4':
    print(dato1, '/', dato2, '=', Dividir(dato1, dato2))
elif choice == '5':
    print(dato1, 'elevado a', dato2, '=', Exponente(dato1, dato2))
else:
    print('Invalid input')