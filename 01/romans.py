#Função que realiza a conversão da variável 'valor' de decimal inteira para algarismos romanos 
def int_to_roman(num):
    inteiros = [
        1000, 900, 500, 400, 
        100, 90, 50, 40,
        10, 9, 5, 4, 
        1
        ]
    romanos = [
        'M', 'CM', 'D', 'CD',
        'C', 'XC', 'L', 'XL',
        'X', 'IX', 'V', 'IV',
        'I'
        ]
    num_roman = ''
    x = 0 

    while num > 0: 
        for _ in range(num // inteiros[x]):
            num_roman += romanos[x]
            num -=inteiros[x]
        x += 1
    return num_roman

#Função que realiza a conversão da variável 'valor' de algarismos romanos para decimal inteira 
def roman_to_int(rom):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_int = 0
    for x in range(len(rom)):
        if x > 0 and roman_dict[rom[x]] > roman_dict[rom[x - 1]]:
            num_int += roman_dict[rom[x]] - 2 * roman_dict[rom[x - 1]]
        else:
            num_int += roman_dict[rom[x]]
    return num_int

#Função onde a variável 'valor' será convertida e escrita na tela 
def convert(valor):
    if valor.isdigit():
        valor = int(valor)
        print('O número decimal inteiro {} convertido para algarismos romanos é: {} '.format(valor, int_to_roman(valor)))
    else:  
        print('Os algarismos romanos {} convertido para seu valor decimal inteiro é: {} '.format(valor, roman_to_int(valor)))

#Usuário digita o valor (romano ou decimal) e o programa armazena na variável 'valor'
valor = input('Digite um número decimal inteiro ou um número em algarismos romanos para realizar a conversão: ')
convert(valor)
