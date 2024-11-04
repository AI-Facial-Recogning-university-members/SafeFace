import sqlite3

type Conn = sqlite3.Connection

# função para conectar ao banco de dados e criar uma tabela de usuarios caso nao exista.
def connect_db() -> Conn:
    conn = sqlite3.connect('funcionarios.db')
    return conn

def create_table() -> None:
    conn = connect_db()
    curr = conn.cursor()

    curr.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios_tbl (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(32),
            cpf VARCHAR(14)
        )
    """)

    conn.commit()
    curr.close()
    conn.close()

#função para adicionar um funcionario
def add_funcionario(nome, cpf) -> None:
    conn = connect_db()
    curr = conn.cursor()

    curr.execute("INSERT INTO funcionarios_tbl(nome, cpf) VALUES(?, ?)", (nome, cpf,))

    conn.commit()
    curr.close()
    conn.close()

# função para remover um funcionario pela busca por cpf
def remover_funcionario(cpf) -> None:
    conn = connect_db()
    curr = conn.cursor()

    curr.execute("DELETE FROM funcionarios_tbl where cpf = ?", (cpf, ))

    conn.commit()
    curr.close()
    conn.close()

# função para selecionar todos os funcionários do BD
def selecionar_funcionarios() -> list:
	conn = connect_db()
	curr = conn.cursor()

	result = curr.execute("SELECT nome, cpf FROM funcionarios_tbl")
	data = result.fetchall()

	conn.commit()
	curr.close()
	conn.close()

	return data
