import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess 

def cadastrar():
    app.destroy()
    subprocess.run(["python", r'.\src\registrePage.py'])


def tableview():
    app.destroy()
    subprocess.run(["python", r'.\src\tablePage.py'])

def executar():
    app.destroy()
    subprocess.run(["python", r'.\src\Main.py'])


app = ttk.Window(themename="superhero")
app.title("SAFEFACE")
app.geometry("750x700")  


label = ttk.Label(app, text="SAFEFACE")
label.grid(row=0, column=0, columnspan=3, pady=35)
label.config(font=("Arial", 30, "bold"))


btn_cadastrar = ttk.Button(app, text="Cadastrar", command=cadastrar,style='PRIMARY')
btn_cadastrar.grid(row=1, column=0, padx=20, pady=20, ipadx=10, ipady=10,sticky="ew")

btn_exdit = ttk.Button(app, text="Regitro de Funcionários", command=tableview,style='PRIMARY')
btn_exdit.grid(row=1, column=1, padx=20, pady=20, ipadx=10, ipady=10,sticky="ew")


btn_executar = ttk.Button(app, text="Executar", command=executar,style='PRIMARY')
btn_executar.grid(row=1, column=2, padx=20, pady=20, ipadx=10, ipady=10,sticky="ew")


app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)


app.mainloop()