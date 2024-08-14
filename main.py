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