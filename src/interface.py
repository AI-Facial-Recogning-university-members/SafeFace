from tkinter import Tk, Label, Entry, Button
from database import add_funcionario

def register_worker() -> None:
	print("saving worker information...")

	name= wname_entry.get()
	cpf= wcpf_entry.get()
	birth_date = wbirth_date_entry.get()

	add_funcionario(wname, wcpf, wbirth_date)

	print("worker info saved")

tk = Tk()
tk.title("Cadastro de funcionário")
tk.geometry("450x320")

wname_label = Label(tk, text="Nome do funcionário")
wcpf_label = Label(tk, text="CPF do funcionário")
wbirth_date_label = Label(tk, text="Data de nascimento do funcionário")

submit_btn = Button(tk, text="Submit", command=register_worker)

wname_entry = Entry(tk)
wcpf_entry = Entry(tk)
wbirth_date_entry = Entry(tk)

wname_label.pack()
wname_entry.pack()
wname_entry.focus_set()

wcpf_label.pack()
wcpf_entry.pack()

wbirth_date_label.pack()
wbirth_date_entry.pack()

submit_btn.pack()

tk.mainloop()
