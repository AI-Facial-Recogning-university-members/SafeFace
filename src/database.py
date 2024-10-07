import sqlite3

# função para conectar ao banco de dados e criar uma tabela de usuarios caso nao exista.
def create_db() -> None:
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER PRIMARY KEY AUTOINCREMENT,nome text NOT NULL, cpf TEXT NOT NULL UNIQUE, dt_nascimento TEXT NOT NULL, imagem_path TEXTO NOT NULL))")

    conn.commit()
    conn.close()

# função para adicionar um funcionario
def add_funcionario(nome, cpf, dt_nascimento, imagem_path) ->  None:
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO funcionarios (nome,cpg,dt_nascimento, imagem_path) VALUES (?,?,?,?)",(nome, cpf, dt_nascimento,imagem_path))

    conn.commit()
    conn.close()

# função para remover um funcionario pela busca por cpf
def remover_funcionario(cpf) -> None:
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE cpf = ?", (cpf))
    conn.commit()
    conn.close()

#função para retornar todos os funcionarios
def get_all_funcionarios() -> None:
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    conn.close()
    return funcionarios
