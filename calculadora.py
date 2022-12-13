print("====calculadora====")

number_1 = int(input('Ente com um valor: '))
print("escolha opcao desejada?")
print(" 1 = add")
print(" 2 = subt")
print(" 3 = div")
print(" 4 = mult")

opcao: str = input("opcao escolhida e ? ")
number_2 = int(input('entre com um valor: '))

if opcao == '1':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

if opcao == '2':
    print('{} - {} ='.format(number_1, number_2))
    print(number_1 - number_2)

if opcao == '3':
    print('{} / {} ='.format(number_1, number_2))
    print(number_1 / number_2)

if opcao == '4':
    print('{} * {} ='.format(number_1, number_2))
    print(number_1 * number_2)

else:
    print('opcao invalida')



