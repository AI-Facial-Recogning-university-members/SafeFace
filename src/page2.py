import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess 
import sqlite3
from database import add_funcionario

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

# Adiciona uma função ao botão "Cadastrar" para chamar salvar_nome com os dados dos campos
def cadastrar():
	nome = nome_entry.get()
	cpf = cpf_entry.get()
	add_funcionario(nome, cpf)

# Outros componentes de interface e o loop principal
def addfoto():
    app.destroy()
    subprocess.run(["python", r'.\src\PrintFace.py'])

def voltar():
    app.destroy()
    subprocess.run(["python", r'.\src\page1.py'])

# Cria a janela principal
app = ttk.Window(title="SAFEFACE", themename="superhero")
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
botoes = ttk.Frame(app)

add_foto_botao = ttk.Button(botoes,text="Add foto", command=addfoto,bootstyle=INFO)
add_foto_botao.pack(side=TOP,pady=10,padx=15)

cadastrar_botao = ttk.Button(botoes, text="Cadastrar", command=cadastrar, bootstyle=SUCCESS)
cadastrar_botao.pack(side=TOP,pady=10,padx=15)

voltar_botao = ttk.Button(botoes, text="Voltar", command=voltar, bootstyle= WARNING)
voltar_botao.pack(side=TOP,pady=10,padx=15)

botoes.pack(pady=30, padx=10, fill="x")

# Inicia o loop principal da janela
app.mainloop()
