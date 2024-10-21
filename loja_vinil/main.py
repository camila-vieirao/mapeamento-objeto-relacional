import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from urllib.parse import quote
from datetime import date
from models.entity import Pessoa, Cliente, Funcionario, Vinil
from models.base import Base

# conecta mysql
instance = f"mysql+pymysql://root:{quote('1234')}@localhost:3301/tde1"
if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autoflush=True, autocommit=False)

# cria db
Base.metadata.create_all(engine)

# CRUD OPS
def perform_crud(entity, operation):
    if operation == 'Create':
        if entity == Pessoa:
            cpf = simpledialog.askstring("Input", "CPF:")
            nome = simpledialog.askstring("Input", "Nome:")
            rg = simpledialog.askstring("Input", "RG:")
            data_nasc = simpledialog.askstring("Input", "Data de Nascimento (YYYY-MM-DD):")
            try:
                pessoa = Pessoa(cpf=cpf, nome=nome, rg=rg, data_nasc=date.fromisoformat(data_nasc))
                session.add(pessoa)
                session.commit()
                messagebox.showinfo("Success", f"Pessoa com CPF {cpf} criada com sucesso!")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro", f"Erro ao criar Pessoa: {e}")

        elif entity == Funcionario:
            cpf = simpledialog.askstring("Input", "CPF:")
            salario = simpledialog.askfloat("Input", "Salário:")
            try:
                funcionario = Funcionario(cpf=cpf, salario=salario)
                session.add(funcionario)
                session.commit()
                messagebox.showinfo("Success", f"Funcionário com CPF {cpf} criado com sucesso!")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro", f"Erro ao criar Funcionário: {e}")

        elif entity == Cliente:
            cpf = simpledialog.askstring("Input", "CPF:")
            endereco = simpledialog.askstring("Input", "Endereço:")
            try:
                cliente = Cliente(cpf=cpf, endereco=endereco)
                session.add(cliente)
                session.commit()
                messagebox.showinfo("Success", f"Cliente com CPF {cpf} criado com sucesso!")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro ao criar Cliente: {e}")

        elif entity == Vinil:
            id = simpledialog.askinteger("Input", "ID:")
            artista = simpledialog.askstring("Input", "Artista:")
            genero = simpledialog.askstring("Input", "Gênero:")
            try:
                vinil = Vinil(id=id, artista=artista, genero=genero)
                session.add(vinil)
                session.commit()
                messagebox.showinfo("Success", f"Vinil com ID {id} criado com sucesso!")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro ao criar Vinil: {e}")

    elif operation == 'Update':
        if entity == Pessoa:
            cpf = simpledialog.askstring("Input", "CPF da pessoa a ser atualizada:")
            pessoa = session.query(Pessoa).filter(Pessoa.cpf == cpf).one_or_none()
            if pessoa:
                nome = simpledialog.askstring("Input", "Nome (deixe vazio para não alterar):")
                rg = simpledialog.askstring("Input", "RG (deixe vazio para não alterar):")
                data_nasc = simpledialog.askstring("Input", "Data de Nascimento (YYYY-MM-DD, deixe vazio para não alterar):")
                
                if nome:
                    pessoa.nome = nome
                if rg:
                    pessoa.rg = rg
                if data_nasc:
                    pessoa.data_nasc = date.fromisoformat(data_nasc)
                
                try:
                    session.commit()
                    messagebox.showinfo("Success", f"Pessoa com CPF {cpf} atualizada com sucesso!")
                except Exception as e:
                    session.rollback()
                    messagebox.showerror("Erro ao atualizar Pessoa: {e}")

        elif entity == Funcionario:
            cpf = simpledialog.askstring("Input", "CPF do funcionário a ser atualizado:")
            funcionario = session.query(Funcionario).filter(Funcionario.cpf == cpf).one_or_none()
            if funcionario:
                salario = simpledialog.askfloat("Input", "Salário (deixe vazio para não alterar):")
                
                if salario is not None:
                    funcionario.salario = salario
                
                try:
                    session.commit()
                    messagebox.showinfo("Success", f"Funcionário com CPF {cpf} atualizado com sucesso!")
                except Exception as e:
                    session.rollback()
                    messagebox.showerror("Erro ao atualizar Funcionário: {e}")

        elif entity == Cliente:
            cpf = simpledialog.askstring("Input", "CPF do cliente a ser atualizado:")
            cliente = session.query(Cliente).filter(Cliente.cpf == cpf).one_or_none()
            if cliente:
                endereco = simpledialog.askstring("Input", "Endereço (deixe vazio para não alterar):")
                
                if endereco:
                    cliente.endereco = endereco
                
                try:
                    session.commit()
                    messagebox.showinfo("Success", f"Cliente com CPF {cpf} atualizado com sucesso!")
                except Exception as e:
                    session.rollback()
                    messagebox.showerror("Erro ao atualizar Cliente: {e}")

        elif entity == Vinil:
            id = simpledialog.askinteger("Input", "ID do vinil a ser atualizado:")
            vinil = session.query(Vinil).filter(Vinil.id == id).one_or_none()
            if vinil:
                artista = simpledialog.askstring("Input", "Artista (deixe vazio para não alterar):")
                genero = simpledialog.askstring("Input", "Gênero (deixe vazio para não alterar):")
                
                if artista:
                    vinil.artista = artista
                if genero:
                    vinil.genero = genero
                
                try:
                    session.commit()
                    messagebox.showinfo("Success", f"Vinil com ID {id} atualizado com sucesso!")
                except Exception as e:
                    session.rollback()
                    messagebox.showerror("Erro ao atualizar Vinil: {e}")

    elif operation == 'Delete':
        if entity == Vinil:
            id = simpledialog.askinteger("Input", "ID para deletar:")
            try:
                vinil = session.query(Vinil).filter(Vinil.id == id).one()
                session.delete(vinil)
                session.commit()
                messagebox.showinfo("Success", f"Vinil com ID {id} deletado com sucesso!")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro ao deletar Vinil: {e}")
        else:
            cpf = simpledialog.askstring("Input", "CPF para deletar:")
            try:
                pessoa = session.query(entity).filter(entity.cpf == cpf).one()
                session.delete(pessoa)
                session.commit()
                messagebox.showinfo("Success", f"{entity.__name__} com CPF {cpf} deletado com sucesso!")
            except Exception as e:
                session.rollback()
                messagebox.showerror("Erro ao deletar {entity.__name__}: {e}")

# REFRESH
def refresh_data(tree, entity):
    # limpa a table e insere os dados novamete
    for row in tree.get_children():
        tree.delete(row)

    if entity == Pessoa:
        records = session.query(Pessoa).all()
        for record in records:
            tree.insert('', 'end', values=(record.cpf, record.nome, record.rg, record.data_nasc))
    elif entity == Funcionario:
        records = session.query(Funcionario).all()
        for record in records:
            tree.insert('', 'end', values=(record.cpf, record.salario))
    elif entity == Cliente:
        records = session.query(Cliente).all()
        for record in records:
            tree.insert('', 'end', values=(record.cpf, record.endereco))
    elif entity == Vinil:
        records = session.query(Vinil).all()
        for record in records:
            tree.insert('', 'end', values=(record.id, record.artista, record.genero))


# MOSTRA OS DADOS
def show_entity_data(root, entity):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Lista de {entity.__name__}", font=("Helvetica", 14)).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=(1, 2, 3, 4), show="headings", height="6")
    tree.pack(side="top", fill=tk.BOTH, expand=True)

    if entity == Pessoa:
        tree.heading(1, text="CPF")
        tree.heading(2, text="Nome")
        tree.heading(3, text="RG")
        tree.heading(4, text="Data de Nascimento")
        records = session.query(Pessoa).all()
        for record in records:
            tree.insert('', 'end', values=(record.cpf, record.nome, record.rg, record.data_nasc))
    elif entity == Funcionario:
        tree.heading(1, text="CPF")
        tree.heading(2, text="Salário")
        records = session.query(Funcionario).all()
        for record in records:
            tree.insert('', 'end', values=(record.cpf, record.salario))
    elif entity == Cliente:
        tree.heading(1, text="CPF")
        tree.heading(2, text="Endereço")
        records = session.query(Cliente).all()
        for record in records:
            tree.insert('', 'end', values=(record.cpf, record.endereco))
    elif entity == Vinil:
        tree.heading(1, text="ID")
        tree.heading(2, text="Artista")
        tree.heading(3, text="Gênero")
        records = session.query(Vinil).all()
        for record in records:
            tree.insert('', 'end', values=(record.id, record.artista, record.genero))

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Create", command=lambda: perform_crud(entity, 'Create')).pack(side="left", padx=5)
    tk.Button(button_frame, text="Update", command=lambda: perform_crud(entity, 'Update')).pack(side="left", padx=5)
    tk.Button(button_frame, text="Delete", command=lambda: perform_crud(entity, 'Delete')).pack(side="left", padx=5)
    tk.Button(button_frame, text="Refresh", command=lambda: refresh_data(tree, entity)).pack(side="left", padx=5)

    tk.Button(root, text="Voltar", command=lambda: main_window(root)).pack(pady=20)


# MAIN MENU
def main_window(root=None):
    if not root:
        root = tk.Tk()
    else:
        for widget in root.winfo_children():
            widget.destroy()

    root.title("CRUD Operations")
    root.geometry("500x400")

    tk.Label(root, text="Selecione uma Entidade:", font=("Helvetica", 14)).pack(pady=10)

    entities_list = ["Pessoa", "Cliente", "Funcionario", "Vinil"]

    entity_frame = tk.Frame(root)
    entity_frame.pack(pady=10)

    tree = ttk.Treeview(entity_frame, columns=(1), show="headings", height=4)
    tree.heading(1, text="Entidade")
    tree.pack(fill="both", expand=True)

    for entity_name in entities_list:
        tree.insert('', 'end', values=(entity_name))

    def on_entity_select(event):
        selected_item = tree.selection()
        entity_name = tree.item(selected_item, 'values')[0]
        entity_mapping = {
            "Pessoa": Pessoa,
            "Cliente": Cliente,
            "Funcionario": Funcionario,
            "Vinil": Vinil
        }
        show_entity_data(root, entity_mapping[entity_name])

    tree.bind('<Double-1>', on_entity_select)

    root.mainloop()


if __name__ == "__main__":
    main_window()
