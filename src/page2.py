import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import subprocess 
import sqlite3

def salvar_nome(nome):
    conn=sqlite3.connect('database.py')
    cursor=conn.cursor()

    cursor.execute('''
                    ''')
    
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



def voltar():
    subprocess.run(["python", "page1.py"])

# Cria a janela principal
app = ttk.Window("SAFEFACE")
app.geometry("550x500")
style = Style(theme="superhero")

# Título
label = ttk.Label(app, text="Cadastro")
label.config(font=("Arial", 20, "bold"))
label.pack(pady=35)

digitNome_func= app.register(validar_nome)
digitCpf_func= app.register(validar_cpf)

# Campo Nome
nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill="x")
ttk.Label(nome, text="Nome").pack(side=LEFT, padx=5)
nome_entry = ttk.Entry(app, validate="focus", validatecommand=(digitNome_func, '%P'))
ttk.Entry(nome).pack(side=LEFT, fill="x", expand=True, padx=5)

# Campo CPF
cpf = ttk.Frame(app)
cpf.pack(pady=18, padx=10, fill="x")
ttk.Label(cpf, text="CPF").pack(side=LEFT, padx=10)
cpf_entry = ttk.Entry(app, validate="focus", validatecommand=(digitCpf_func, '%P'))
ttk.Entry(cpf).pack(side=LEFT, fill="x", expand=True, padx=5)


# Botões
botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill="x")
ttk.Button(botao, text="Cadastrar", command=cadastrar, bootstyle=SUCCESS).pack(side=LEFT, padx=15)
ttk.Button(botao, text="Voltar", command=voltar,bootstyle=SUCCESS).pack(side=LEFT, padx=15)

# Inicia o loop principal da janela
app.mainloop()
