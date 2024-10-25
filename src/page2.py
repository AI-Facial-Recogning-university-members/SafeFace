import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess 
from database import add_funcionario

def salvar_nome():
	add_funcionario(nome_entry.get(), cpf_entry.get())

def validar_nome(x)-> bool:
    if x.isdigit():
        return True
    elif x == "":
        return True
    else:
        return False
    
def validar_cpf(x)-> bool:
    if x.isdigit():
        return False
    elif x == "":
        return True
    else:
        return True

def addfoto():
    subprocess.run(["python",r'.\src\PrintFace.py'])

def voltar():
    subprocess.run(["python", r'.\src\page1.py'])

# Cria a janela principal
app = ttk.Window(title="SAFEFACE", themename="superhero")
app.geometry("750x700")

digitNome_func= app.register(validar_nome)
digitCpf_func= app.register(validar_cpf)

# Título
label = ttk.Label(app, text="Cadastro")
label.config(font=("Arial", 20, "bold"))
label.pack(pady=35)

campos = ttk.Frame(app)

# Frame Nome
nome_frame = ttk.Frame(app)

# Campo Nome
nome_label = ttk.Label(campos, text="Nome")
nome_label.pack(side=LEFT, padx=5)

nome_entry = ttk.Entry(campos)
nome_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

nome_frame.pack()

# Frame CPF
cpf_frame = ttk.Frame(app)

# Campo CPF
cpf_label = ttk.Label(campos, text="CPF")
cpf_label.pack(side=LEFT, padx=10)

cpf_entry = ttk.Entry(campos, validate="focus", validatecommand=(digitCpf_func, '%P'))
cpf_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

campos.pack(pady=18, padx=10, fill="x")

cpf_frame = ttk.Frame(app)
# Botões
botoes = ttk.Frame(app)

add_foto_botao = ttk.Button(botoes,text="Add foto", command=addfoto,bootstyle=SUCCESS)

cadastrar_botao = ttk.Button(botoes, text="Cadastrar", command=salvar_nome, bootstyle=SUCCESS)
cadastrar_botao.pack(side=TOP,pady=10,padx=15)

voltar_botao = ttk.Button(botoes, text="Voltar", command=voltar, bootstyle=WARNING)
voltar_botao.pack(side=BOTTOM,pady=10,padx=30)

botoes.pack(pady=30, padx=10, fill="x")

# Inicia o loop principal da janela
app.mainloop()
