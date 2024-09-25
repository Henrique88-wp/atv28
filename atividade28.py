# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar


produto = []
estoque = []


for i in range(5):
    a = input(f"Coloque o produto {i+1}: ")
    quanto = int(input(f"Coloque a quantidade do produto {i+1}: ")) 
    produto.append(a)
    estoque.append(quanto)

nao_ha = []


for i in range(5):
    if estoque[i] == 0:
        nao_ha.append(produto[i])


if nao_ha:
    print(f"Produtos com estoque zerado: {', '.join(nao_ha)}")
else:
    print("Todos estão em dia, chefe.")
