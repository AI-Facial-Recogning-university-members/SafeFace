import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ttkbootstrap.tableview import Tableview 
import subprocess 
import sqlite3

app = ttk.Window(themename="superhero",title="SAFEFACE")
app.geometry("750x500")
colors = app.style.colors


l1 = [
    {"text": "Nome", "stretch": True},
    {"text": "CPF", "stretch": False},
]

r_set = [
    ("teste",1234567),
    ("teste",1264567),
    ("teste",1244567),
]


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

app.mainloop()
