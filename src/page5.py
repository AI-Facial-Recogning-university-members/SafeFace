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

nome_entry = ttk.Entry(app)
nome_entry.pack()

cpf_frame = ttk.Frame(app)
cpf_frame.pack()

cpf_label = ttk.Label(app, text="CPF: ")
cpf_label.pack()

cpf_entry = ttk.Entry(app)
cpf_entry.pack()

botao_excluir = ttk.Button(app, text="Excluir", command=delfuncionario)
botao_excluir.pack()

aviso_label = ttk.Label(app)
aviso_label.config(font=("arial", 15, "bold"))
aviso_label.pack(pady=35)

app.mainloop()
