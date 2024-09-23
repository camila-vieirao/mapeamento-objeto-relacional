from services.database import session
from crudoperations.pessoa import create_pessoa, read_pessoa, update_pessoa, delete_pessoa
from crudoperations.funcionario import create_funcionario, read_funcionario, update_funcionario, delete_funcionario
from crudoperations.cliente import create_cliente, read_cliente, update_cliente, delete_cliente
from crudoperations.vinil import create_vinil, read_vinil, update_vinil, delete_vinil
from models import Pessoa, Funcionario, Cliente, Vinil
from datetime import date

def crud_op(entidade):
    while True:
        print("=======  MENU CRUD =====")
        print(" Escolha uma operação CRUD:")
        print("  1. Create")
        print("  2. Read")
        print("  3. Update")
        print("  4. Delete")
        print("  5. Voltar")

        op = input("\nOpção: ")
        
        if op == "1":
            if entidade == Pessoa:
                cpf = input("CPF: ")
                nome = input("Nome: ")
                rg = input("RG: ")
                data_nasc = input("Data de Nascimento (YYYY-MM-DD): ")
                create_pessoa(session, cpf, nome, rg, date.fromisoformat(data_nasc))
            elif entidade == Funcionario:
                cpf = input("CPF: ")
                salario = float(input("Salário: "))
                create_funcionario(session, cpf, salario)
            elif entidade == Cliente:
                cpf = input("CPF: ")
                endereco = input("Endereço: ")
                create_cliente(session, cpf, endereco)
            elif entidade == Vinil:
                id = int(input("ID: "))
                artista = input("Artista: ")
                genero = input("Gênero: ")
                create_vinil(session, id, artista, genero)
        elif op == "2":
            if entidade == Pessoa:
                cpf = input("CPF: ")
                read_pessoa(session, cpf)
            elif entidade == Funcionario:
                cpf = input("CPF: ")
                read_funcionario(session, cpf)
            elif entidade == Cliente:
                cpf = input("CPF: ")
                read_cliente(session, cpf)
            elif entidade == Vinil:
                id = int(input("ID: "))
                read_vinil(session, id)
        elif op == "3":
            if entidade == Pessoa:
                cpf = input("CPF: ")
                nome = input("Nome (deixe em branco para não atualizar): ")
                rg = input("RG (deixe em branco para não atualizar): ")
                data_nasc = input("Data de Nascimento (YYYY-MM-DD, deixe em branco para não atualizar): ")
                update_pessoa(session, cpf, nome or None, rg or None, date.fromisoformat(data_nasc) if data_nasc else None)
            elif entidade == Funcionario:
                cpf = input("CPF: ")
                salario = input("Salário (deixe em branco para não atualizar): ")
                update_funcionario(session, cpf, float(salario) if salario else None)
            elif entidade == Cliente:
                cpf = input("CPF: ")
                endereco = input("Endereço (deixe em branco para não atualizar): ")
                update_cliente(session, cpf, endereco or None)
            elif entidade == Vinil:
                id = int(input("ID: "))
                artista = input("Artista (deixe em branco para não atualizar): ")
                genero = input("Gênero (deixe em branco para não atualizar): ")
                update_vinil(session, id, artista or None, genero or None)
        elif op == "4":
            if entidade == Pessoa:
                cpf = input("CPF: ")
                delete_pessoa(session, cpf)
            elif entidade == Funcionario:
                cpf = input("CPF: ")
                delete_funcionario(session, cpf)
            elif entidade == Cliente:
                cpf = input("CPF: ")
                delete_cliente(session, cpf)
            elif entidade == Vinil:
                id = int(input("ID: "))
                delete_vinil(session, id)
        elif op == "5":
            print("Voltando ao menu inicial...")
            return
        elif op == "6":
            print("Tchau! :]")
            exit(0)
