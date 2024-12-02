import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview 
import subprocess 
import sqlite3
from database import selecionar_funcionarios

app = ttk.Window(themename="superhero",title="SAFEFACE - Registros")
app.geometry("800x880")
colors = app.style.colors

label = ttk.Label(app, text="Editor de dados")
label.config(font=("arial", 20, "bold"))
label.pack(pady=35)

def editar():
    app.destroy()
    subprocess.run(["python", r'.\src\exditPage.py'])

def excluir():
	app.destroy()
	subprocess.run(["python", r'.\src\deletePage.py'])

def voltar():
    app.destroy()
    subprocess.run(["python", r'.\src\main.py'])

l1 = [
    {"text": "Nome", "stretch": True},
    {"text": "CPF", "stretch": False},
	{"text": "Clock in", "stretch": False}
]

r_set = selecionar_funcionarios()

tv = Tableview(
    master=app,
    coldata=l1,
    rowdata=r_set,
    pagesize=10,
    height=10,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(None, None))
tv.autofit_columns()
tv.pack(fill=BOTH, expand=YES, padx=10, pady=10)

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill="x")
ttk.Button(botao,text="Editar", command=editar,bootstyle=INFO).pack(side=TOP,pady=10,padx=15)
ttk.Button(botao,text="Excluir", command=excluir,bootstyle=WARNING).pack(side=TOP,pady=10,padx=15)
ttk.Button(botao,text="Voltar", command=voltar,bootstyle=SUCCESS).pack(side=TOP,pady=10,padx=15)
app.mainloop()
