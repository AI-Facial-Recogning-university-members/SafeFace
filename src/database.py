import sqlite3

#função para conectar ao banco de dados e criar uma tabela de usuarios caso nao exista.
def connect_db() -> sqlite3.Connection:
    conn = sqlite3.connect('funcionarios.db')
    return conn

def create_table() -> None:
    conn = connect_db()
    curr = conn.cursor()

    curr.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios_tbl (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(32),
            cpf VARCHAR(14),
            dt_nascimento TEXT
        )
    """)

    conn.commit()
    curr.close()
    conn.close()

#função para adicionar um funcionario
def add_funcionario(nome, cpf, dt_nascimento) -> None:
    conn = connect_db()
    curr = conn.cursor()

    curr.execute("INSERT INTO funcionarios_tbl(nome, cpf, dt_nascimento) VALUES(?, ?, ?)", (nome, cpf, dt_nascimento))

    conn.commit()
    curr.close()
    conn.close()

#função para remover um funcionario pela busca por cpf
def remover_funcionario(cpf):
    raise NotImplementedError

#função para retornar todos os funcionarios
def get_all_funcionarios():
    raise NotImplementedError