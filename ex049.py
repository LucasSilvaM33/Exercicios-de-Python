'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for.'''


cont = 0 #contador começa em zero
num = int(input('Digite um número inteiro: ')) #leio o número inteiro do usuário

for c in range(1, 11): #coloco o comando de repetição, fazendo isso de 1 até 10
    cont = cont + 1 #pego o meu contador que está em 0 e adiciono +1, isso vai fazer com que ele faça uma contagem até a 10, devido ao comando repetição
    print(f'{num} x {cont} = {cont * num}')