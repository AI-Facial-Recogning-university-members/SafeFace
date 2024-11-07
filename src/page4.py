import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess 
from database import atualizar_registro, verificar_info

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
	nome_antigo = nome_entry.get()
	cpf_antigo = cpf_entry.get()
	nome_novo = nome_novo_entry.get()
	cpf_novo = cpf_novo_entry.get()

	# se o usuário já existir ele vai estar
	# registrado com "cpf_antigo"
	if(verificar_info(cpf_antigo) != 1):
		aviso_label.config(text="Usuário não encontrado.")
	else:
		atualizar_registro(nome_antigo, cpf_antigo, nome_novo, cpf_novo)

def voltar():
    app.destroy()
    subprocess.run(["python", r'.\src\page1.py'])

# Função da tela de cadastro
def tela_cadastro():
    global app, nome_entry, cpf_entry, nome_novo_entry, cpf_novo_entry, aviso_label
    app = ttk.Window(title="SAFEFACE - Cadastro", themename="superhero")
    app.geometry("750x700")

    # Título
    label = ttk.Label(app, text="Cadastro")
    label.config(font=("arial", 20, "bold"))
    label.pack(pady=35)

    digitNome_func = app.register(validar_nome)
    digitCpf_func = app.register(validar_cpf)

    # Campo Nome Atual
    nome = ttk.Frame(app)
    nome.pack(pady=18, padx=10, fill="x")
    ttk.Label(nome, text="Nome").pack(side=LEFT, padx=5)
    nome_entry = ttk.Entry(nome, validate="focus", validatecommand=(digitNome_func, '%P'))
    nome_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

    # Campo CPF Atual
    cpf = ttk.Frame(app)
    cpf.pack(pady=18, padx=10, fill="x")
    ttk.Label(cpf, text="CPF").pack(side=LEFT, padx=10)
    cpf_entry = ttk.Entry(cpf, validate="focus", validatecommand=(digitCpf_func, '%P'))
    cpf_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

    # Campo Nome Novo
    nome_novo = ttk.Frame(app)
    nome_novo.pack(pady=18, padx=10, fill="x")
    ttk.Label(nome, text="Nome novo").pack(side=LEFT, padx=5)
    nome_novo_entry = ttk.Entry(nome, validate="focus", validatecommand=(digitNome_func, '%P'))
    nome_novo_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

    # Campo CPF Novo
    cpf_novo = ttk.Frame(app)
    cpf_novo.pack(pady=18, padx=10, fill="x")
    ttk.Label(cpf, text="CPF").pack(side=LEFT, padx=10)
    cpf_novo_entry = ttk.Entry(cpf, validate="focus", validatecommand=(digitCpf_func, '%P'))
    cpf_novo_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

    # Botões
    botao = ttk.Frame(app)
    botao.pack(pady=30, padx=10, fill="x")
    ttk.Button(botao, text="Editar foto", command=editarfoto, bootstyle=SUCCESS).pack(side=TOP, pady=10, padx=15)
    ttk.Button(botao, text="Atualizar", command=atualizar, bootstyle=INFO).pack(side=TOP, pady=10, padx=15)
    ttk.Button(botao, text="Voltar ao Inicio", command=voltar, bootstyle=WARNING).pack(side=BOTTOM, pady=10, padx=30)

	# Avisos de erro
    aviso_label = ttk.Label(app)
    aviso_label.config(font=("arial", 15, "bold"))
    aviso_label.pack(pady=35)

    app.mainloop()

# Inicializa diretamente a tela de cadastro
tela_cadastro()
