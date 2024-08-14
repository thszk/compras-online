from model.cliente import Cliente

lista_cliente = []

def cadastrar():
    novo_cliente = Cliente('Fulano 1')

    lista_cliente.append(novo_cliente)


def listar():
    print('-----Clientes-----')
    for cliente in lista_cliente:
        print(f'nome: {cliente.nome}')

    print()