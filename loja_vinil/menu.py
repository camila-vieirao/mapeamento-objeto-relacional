import crud
from models.pessoa import Pessoa
from models.funcionario import Funcionario
from models.cliente import Cliente
from models.vinil import Vinil

def menu_inicial():
    while True:
        print("Bem-vindo!")
        print("Escolha uma entidade para começar:")
        print("  1. Cliente")
        print("  2. Funcionário")
        print("  3. Pessoa")
        print("  4. Vinil")
        print("  5. Sair")

        op = input("\nOpção: ")
        
        if op == "1":
            entidade = Cliente
        elif op == "2":
            entidade = Funcionario
        elif op == "3":
            entidade = Pessoa
        elif op == "4":
            entidade = Vinil
        elif op == "5":
            print("Tchau! :]")
            exit(0)
        else:
            print("Opção inválida, tente novamente.")
            continue
        
        crud.crud_op(entidade)
