import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess 
import sqlite3

# Função para salvar nome e cpf no banco de dados
def salvar_nome(nome, cpf):
    conn = sqlite3.connect('database.py')  # Nome do arquivo de banco de dados
    curr = conn.cursor()
    curr.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios_tbl (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           nome VARCHAR(32),
           cpf VARCHAR(14)
        )
    ''')
    curr.execute("INSERT INTO funcionarios_tbl(nome, cpf) VALUES(?, ?)", (nome, cpf,))
    conn.commit()
    conn.close()

# Função que valida o nome
def validar_nome(x) -> bool:
    if x.isdigit():
        return False
    elif x == "":
        return True
    else:
        return True

# Função que valida o CPF
def validar_cpf(x) -> bool:
    if x.isdigit() or x == "":
        return True
    return False

# Função para editar foto
def editarfoto():
    subprocess.run(["python", r'.\src\PrintFace.py'])


# Função para atualizar dados
def atualizar():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    salvar_nome(nome, cpf)

def voltar():
    app.destroy()
    subprocess.run(["python", r'.\src\page1.py'])


# Função da tela de cadastro
def tela_cadastro():
    global app, nome_entry, cpf_entry
    app = ttk.Window(title="SAFEFACE - Cadastro", themename="superhero")
    app.geometry("750x700")

    # Título
    label = ttk.Label(app, text="Cadastro")
    label.config(font=("Arial", 20, "bold"))
    label.pack(pady=35)

    digitNome_func = app.register(validar_nome)
    digitCpf_func = app.register(validar_cpf)

    # Campo Nome
    nome = ttk.Frame(app)
    nome.pack(pady=18, padx=10, fill="x")
    ttk.Label(nome, text="Nome").pack(side=LEFT, padx=5)
    nome_entry = ttk.Entry(nome, validate="focus", validatecommand=(digitNome_func, '%P'))
    nome_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

    # Campo CPF
    cpf = ttk.Frame(app)
    cpf.pack(pady=18, padx=10, fill="x")
    ttk.Label(cpf, text="CPF").pack(side=LEFT, padx=10)
    cpf_entry = ttk.Entry(cpf, validate="focus", validatecommand=(digitCpf_func, '%P'))
    cpf_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

    # Botões
    botao = ttk.Frame(app)
    botao.pack(pady=30, padx=10, fill="x")
    ttk.Button(botao, text="Editar foto", command=editarfoto, bootstyle=SUCCESS).pack(side=TOP, pady=10, padx=15)
    ttk.Button(botao, text="Atualizar", command=atualizar, bootstyle=INFO).pack(side=TOP, pady=10, padx=15)
    ttk.Button(botao, text="Voltar ao Inicio", command=voltar, bootstyle=WARNING).pack(side=BOTTOM, pady=10, padx=30)

    app.mainloop()

# Inicializa diretamente a tela de cadastro
tela_cadastro()
