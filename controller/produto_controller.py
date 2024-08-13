from model.produto import Produto

lista_produtos = []

def cadastrar():

    novo_produto = Produto('Bola', 3.99)

    lista_produtos.append(novo_produto)

def listar():
    print('-----Produtos-----')
    for produto in lista_produtos:
        print(f'nome: {produto.nome}, preço: {produto.preco}')

    print()