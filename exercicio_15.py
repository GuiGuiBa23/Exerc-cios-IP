numero = int(input('Digite seu número: '))
print('---Solução com FOR---')
for m in range (1,11):
        print(f'{numero} x {m} = {numero * m} ')

# OU

numero = int(input('Digite seu número: '))
print('---Solução com FOR---')
for m in range (1,11):
        resultado = numero * m
        print(f'{numero} x {m} = {resultado} ')


print('---Solução com WHILE---')
ciclos = 1

while ciclos <= 10:
    resultado = numero * ciclos
    print(f'{numero} x {ciclos} = {resultado}')
    # incremento
    ciclos += 1