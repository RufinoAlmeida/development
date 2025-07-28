# importando SQLite
import sqlite3 as lite

# Conectando ao banco de dados
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizada com sucesso!')
except lite.Error as e:
    print('Erro ao conectar com o banco de dados:', e)

# ---------------- TABELA DE CURSOS ----------------

# Criar curso (Create)
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Cursos (nome, duracao, preco) VALUES (?, ?, ?)'
        cur.execute(query, i)

# Ver cursos (Read)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linhas = cur.fetchall()
        for i in linhas:
            lista.append(i)
    return lista

# Atualizar curso (Update)
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?'
        cur.execute(query, i)

# Deletar curso (Delete)
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Cursos WHERE id=?'
        cur.execute(query, i)

# ---------------- TABELA DE TURMAS ----------------

# Criar turma (Create)
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Turmas (nome, turma_nome, data_inicio) VALUES (?, ?, ?)'
        cur.execute(query, i)

# Ver turmas (Read)
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linhas = cur.fetchall()
        for i in linhas:
            lista.append(i)
    return lista

# Atualizar turma (Update)
def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE Turmas SET nome=?, data_inicio=? WHERE id=?'
        cur.execute(query, i)

# Deletar turma (Delete)
def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Turmas WHERE id=?'
        cur.execute(query, i)

# ---------------- TABELA DE ALUNOS ----------------

# Criar aluno (Create)
def criar_aluno(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        cur.execute(query, i)

# Ver alunos (Read)
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linhas = cur.fetchall()
        for i in linhas:
            lista.append(i)
    return lista

# Atualizar aluno (Update)
def atualizar_aluno(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE Alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?'
        cur.execute(query, i)

# Deletar aluno (Delete)
def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Alunos WHERE id=?'
        cur.execute(query, i)
