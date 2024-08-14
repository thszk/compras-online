import controller.produto_controller as produto_controller
import controller.cliente_controller as cliente_controller

cliente_controller.cadstrar()
cliente_controller.adicionar_no_carrinho()

def menu_admin():
    while True:
        print('Menu Admin')
        print('1. Cadastro produto')
        print('2. Listar produto')
        print('0. Voltar')

        op_admin = int(input('> '))

        match op_admin:
            case 1:
                produto_controller.cadastrar()
            case 2:
                produto_controller.listar()
            case 0:
                break


menu_admin()

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
