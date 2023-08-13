'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


sexo = str(input('Informe  seu sexo: [M/F]')).strip().upper()[0] #[0] uuqer dizer que o programa vai pegar a primeira letra da palavra masculimo ou feminino
while sexo not in 'MmFf':
     sexo = str(input('Sexo inválido. Por favor digite o sexo novamente: ')).strip().upper()
print(f'O sexo {sexo} foi registrado com sucesso! ')

