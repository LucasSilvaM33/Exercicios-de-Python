#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 1.75,  #perceba que todos os produtos estão na posição par e os preços nas ímpares. Esse raciocínio vai ser necessário para resolver o problema
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.30,
            'Canetas', 22.30,
            'Livros', 34.90)
print('-' * 40)
print(f'{"LISTAGENS DE PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)): #Aqui a gente faz a númeração (posição) dos itens da listagem, que começa em 0 e vai até a quantidades de itens da listagem(isso inclui os produtos e preços)
    #por isso range vai de 0 até 18. len(listagem) = 18
    if pos % 2 == 0: #Aqui eu vou selecionar todos os itens que estão na posição par
        print(f'{listagem[pos] :.<40}', end=' ') #Aqui eu mostro quais são esses itens
    else:
        print(f'R$ {listagem[pos]}') #Aqui mostro os itens da posição ímpar
