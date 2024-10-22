import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess 

def cadastrar():
    subprocess.run(["python", "page2.py"])

def exdit():
    print("Excluir botão pressionado!")

def executar():
    subprocess.run(["python", "PrintFace.py"])


app = ttk.Window(themename="superhero")
app.title("SAFEFACE")
app.geometry("750x700")  


label = ttk.Label(app, text="SAFEFACE")
label.grid(row=0, column=0, columnspan=3, pady=35)
label.config(font=("Arial", 30, "bold"))



btn_cadastrar = ttk.Button(app, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=1, column=0, padx=20, pady=20, ipadx=10, ipady=10)

btn_exdit = ttk.Button(app, text="Excluir ou Editar", command=exdit)
btn_exdit.grid(row=1, column=1, padx=20, pady=20, ipadx=10, ipady=10)

btn_executar = ttk.Button(app, text="Executar", command=executar)
btn_executar.grid(row=1, column=2, padx=20, pady=20, ipadx=10, ipady=10)

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)


app.mainloop()
