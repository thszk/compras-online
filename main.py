import controller.produto_controller as produto_controller
import controller.cliente_controller as cliente_controller


produto_controller.cadastrar()
produto_controller.listar()

while True:
    print('Menu Principal')
    print('1. Cadastro cliente')
    print('2. Listar cliente')
    print('0. Sair')

    op = int(input('> '))

    match op:
        case 1:
            cliente_controller.cadastrar()
        case 2:
            cliente_controller.listar()
        case 0:
            break
