"""Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""


expr = str(input('Digite a xpressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')


    elif simb == ')':
        if len(pilha) > 0: #A pilha não está vazia
            pilha.pop() #Vamos remover o ultimo elemento
        else:
            pilha.append(')') #Se a pilha estiver vazia, adiciona o ) fechando a equação
            break
if len(pilha) == 0:
    print('Sua expressão está correta! ')
else:
    print('Sua expressão está errada! ')


