import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview 
import subprocess 
import sqlite3
from database import selecionar_funcionarios

app = ttk.Window(themename="superhero",title="SAFEFACE")
app.geometry("750x500")
colors = app.style.colors

def editar():
    app.destroy()
    subprocess.run(["python", r'.\src\page4.py'])

def excluir():
	app.destroy()
	subprocess.run(["python", r'.\src\page5.py'])


l1 = [
    {"text": "Nome", "stretch": True},
    {"text": "CPF", "stretch": False},
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
ttk.Button(botao,text="Editar", command=editar,bootstyle=SUCCESS).pack(side=TOP,pady=10,padx=15)
ttk.Button(botao,text="Excluir", command=excluir,bootstyle=SUCCESS).pack(side=TOP,pady=10,padx=15)
app.mainloop()
