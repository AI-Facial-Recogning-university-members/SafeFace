import sqlite3

# função para conectar ao banco de dados e criar uma tabela de usuarios caso nao exista.
def connect_db() -> sqlite3.Connection:
	# Nome do arquivo de banco de dados
	conn = sqlite3.connect('funcionarios.db')
	return conn

def create_table() -> None:
	conn = connect_db()
	curr = conn.cursor()

    # Cria a tabela, caso não exista
	curr.execute("""
		CREATE TABLE IF NOT EXISTS funcionarios_tbl (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			nome VARCHAR(32),
			cpf VARCHAR(14) UNIQUE
		)
    """)

	conn.commit()
	curr.close()
	conn.close()

#função para adicionar um funcionario
def add_funcionario(nome, cpf) -> None:
	create_table()
	conn = connect_db()
	curr = conn.cursor()

	# Insere os dados na tabela
	curr.execute("INSERT INTO funcionarios_tbl(nome, cpf) VALUES(?, ?)", (nome, cpf,))

	conn.commit()	# Salva as alterações
	curr.close()	# Fecha o cursor
	conn.close()	# Fecha a conexão

# função para remover um funcionario pela busca por cpf
def remover_funcionario(cpf) -> None:
	create_table()
	conn = connect_db()
	curr = conn.cursor()

	curr.execute("DELETE FROM funcionarios_tbl where cpf = ?", (cpf, ))

	conn.commit()
	curr.close()
	conn.close()

# função para selecionar todos os funcionários do BD
def selecionar_funcionarios() -> list:
	create_table()
	conn = connect_db()
	curr = conn.cursor()

	result = curr.execute("SELECT nome, cpf FROM funcionarios_tbl")
	data = result.fetchall()

	conn.commit()
	curr.close()
	conn.close()

	return data

# Função para salvar nome e cpf no banco de dados
def atualizar_registro(nome_antigo, cpf_antigo, nome_novo, cpf_novo):
	create_table()
	conn = connect_db()
	curr = conn.cursor()

	curr.execute("UPDATE funcionarios_tbl SET nome = ?, cpf = ? WHERE nome = ? AND cpf = ?", (nome_novo, cpf_novo, nome_antigo, cpf_antigo,))

	conn.commit()
	conn.close()

def deletar_funcionario(nome_funcionario, cpf_funcionario):
	create_table()
	conn = connect_db()
	curr = conn.cursor()

	curr.execute("DELETE FROM funcionarios_tbl WHERE nome = ? AND cpf = ?", (nome_funcionario, cpf_funcionario,))

	conn.commit()
	curr.close()
	conn.close()

# Função que procura o nome no banco de dados
def verificar_info(nome_procurar, cpf_procurar):
	create_table()
	conn = connect_db()
	curr = conn.cursor()

	curr.execute("SELECT COUNT(*) FROM funcionarios_tbl WHERE nome = ? AND cpf = ?", (nome_procurar, cpf_procurar,))
	resultado = curr.fetchone()

	conn.commit()
	curr.close()
	conn.close()

	return resultado[0]
