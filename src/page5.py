import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from database import deletar_funcionario, verificar_info

def delfuncionario():
	if verificar_info(nome_entry.get(), cpf_entry.get()) == 0:
		aviso_label.config(text="Usuário não encontrado.")
	else:
		deletar_funcionario(nome_entry.get(), cpf_entry.get())

app = ttk.Window(title="SAFEFACE - exclusão", themename="superhero")
app.geometry("750x700")

titulo_label = ttk.Label(app, text="Exclusão de funcionários")
titulo_label.config(font=("arial", 20, "bold"))
titulo_label.pack(padx=35, pady=10)

nome_label = ttk.Label(app, text="Nome: ")
nome_label.pack()

nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill="x")
ttk.Label(nome, text="Nome").pack(side=LEFT, padx=5)
nome_entry = ttk.Entry(nome, validate="focus")
nome_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

# Campo CPF
cpf = ttk.Frame(app)
cpf.pack(pady=18, padx=10, fill="x")
ttk.Label(cpf, text="CPF").pack(side=LEFT, padx=10)
cpf_entry = ttk.Entry(cpf, validate="focus")
cpf_entry.pack(side=LEFT, fill="x", expand=True, padx=5)

botao_excluir = ttk.Button(app, text="Excluir", command=delfuncionario)
botao_excluir.pack()

aviso_label = ttk.Label(app)
aviso_label.config(font=("arial", 15, "bold"))
aviso_label.pack(pady=35)

app.mainloop()
