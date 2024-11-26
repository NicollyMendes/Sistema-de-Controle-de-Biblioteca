import sqlite3
from datetime import datetime

def connect():
    conexao = sqlite3.connect('dados_biblioteca.db')
    return conexao

# Funções para manipulação dos dados no banco

# Função para inserir um livro
def insert_book(titulo, autor, editora, ISBN, ano_de_publicacao, genero, quantidade_disponivel):
    conexao = connect()
    conexao.execute('INSERT INTO Livros(titulo, autor, editora, isbn, ano_de_publicacao, genero, quantidade_disponivel) VALUES (?,?,?,?,?,?,?)',
                    (titulo, autor, editora, ISBN, ano_de_publicacao, genero, quantidade_disponivel))
    conexao.commit()
    conexao.close()

# Função para visualizar todos os livros cadastrados
def get_books():
    conexao = connect()
    c = conexao.cursor()
    c.execute('SELECT id_livro, titulo, autor, editora, ano_de_publicacao,isbn, quantidade_disponivel FROM Livros')
    livros = c.fetchall()
    conexao.close()
    return livros

# Função para buscar livros com filtros
def search_books(titulo=None, autor=None, editora=None, ano_de_publicacao=None, genero=None):
    conexao = connect()
    c = conexao.cursor()
    
    query = "SELECT * FROM Livros WHERE 1=1"  # Base inicial que sempre é verdadeira
    lista = []
    
    if titulo:
        query += " AND titulo LIKE ?"
        lista.append(f"%{titulo}%")
    if autor:
        query += " AND autor LIKE ?"
        lista.append(f"%{autor}%")
    if editora:
        query += " AND editora LIKE ?"
        lista.append(f"%{editora}%")
    if ano_de_publicacao:
        query += " AND ano_de_publicacao = ?"
        lista.append(ano_de_publicacao)
    if genero:
        query += " AND genero LIKE ?"
        lista.append(f"%{genero}%")
    
    c.execute(query, lista)
    resultado = c.fetchall()
    conexao.close()
    return resultado

# Função para inserir um novo usuário
def insert_user(nome, sobrenome, endereco, email, telefone):
    conexao = connect()
    conexao.execute('INSERT INTO Usuarios(nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)',\
                    (nome, sobrenome, endereco, email, telefone))
    conexao.commit()
    conexao.close()

# Função para visualizar todos os usuários cadastrados
def get_users():
    conexao = connect()
    c = conexao.cursor()
    c.execute('SELECT * FROM Usuarios')
    usuarios = c.fetchall()
    conexao.close()
    return usuarios

# Função para editar dados de um usuário
def update_user(id_usuario, nome, sobrenome, endereco, email, telefone):
    conexao = connect()
    conexao.execute('UPDATE Usuarios SET nome = ?, sobrenome = ?, endereco = ?, email = ?, telefone = ? WHERE id_usuario = ?',\
                    (nome, sobrenome, endereco, email, telefone, id_usuario))
    conexao.commit()
    conexao.close()

# Função para realizar um empréstimo
def insert_loan(id_usuario, id_livro, data_emprestimo, data_devolucao_prevista, status):
    conexao = connect()
    conexao.execute('INSERT INTO Emprestimos(id_usuario, id_livro, data_emprestimo, data_devolucao_prevista, status) VALUES (?, ?, ?, ?, ?)',\
                    (id_usuario, id_livro, data_emprestimo, data_devolucao_prevista, status))
    conexao.commit()
    conexao.close()

# Função para visualizar livros atualmente emprestados
def get_books_loan():
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('''SELECT Emprestimos.id_emprestimo, Livros.titulo, Usuarios.nome, 
                             Emprestimos.data_emprestimo, Emprestimos.data_devolucao_prevista
                      FROM Emprestimos
                      JOIN Livros ON Emprestimos.id_livro = Livros.id_livro
                      JOIN Usuarios ON Emprestimos.id_usuario = Usuarios.id_usuario
                      WHERE Emprestimos.data_devolucao_real IS NULL''')
    resultados = cursor.fetchall()  # Extraí os dados
    conexao.close()
    return resultados

#Função para atualizar a data de devolucao do emprestimo
def update_loan_return_date(emprestimo_id, data_devolucao_real):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('UPDATE Emprestimos SET data_devolucao_real = ? WHERE id_emprestimo = ?', 
                   (data_devolucao_real, emprestimo_id))
    conexao.commit()
    conexao.close()
#Função para obter a data de vencimento  de um emprestimo especifico 
def get_loan_due_date(emprestimo_id):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT data_devolucao_prevista FROM Emprestimos WHERE id_emprestimo = ?', (emprestimo_id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return datetime.strptime(resultado[0], '%Y-%m-%d').date()  # Converte para objeto datetime.date
    return None
#Função para obter a data de devolucao real de um emprestimo especifico
def get_loan_return_date(emprestimo_id):
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute('SELECT data_devolucao_real FROM Emprestimos WHERE id_emprestimo = ?', (emprestimo_id,))
    resultado = cursor.fetchone()  # Retorna uma tupla ou None
    conexao.close()
    if resultado and resultado[0]:  # Verifica se há um resultado válido
        return datetime.strptime(resultado[0], '%Y-%m-%d').date()  # Converte para objeto date
    return None

#Função para inserir reservas
def insert_reservation(id_usuario, id_livro, data_reserva, status_reserva):
    conexao = connect()
    conexao.execute('INSERT INTO Reservas(id_usuario, id_livro, data_reserva, status_reserva) VALUES (?, ?, ?, ?)'\
                    ,(id_usuario, id_livro, data_reserva, status_reserva))
    conexao.commit()
    conexao.close()

#Função para exibir as reservas 
def get_reservations():
    conexao = connect()
    c = conexao.cursor()
    c.execute('SELECT * FROM Reservas')
    reservas = c.fetchall()
    conexao.close()
    return reservas

#Função para atualizar as reservas
def update_reservation_status(id_reserva, status_reserva):
    conexao = connect()
    conexao.execute('UPDATE Reservas SET status_reserva = ? WHERE id_reserva = ?',\
                    (status_reserva, id_reserva))
    conexao.commit()
    conexao.close()

#Função para inserir multas
def insert_fine(id_emprestimo, valor, status_pagamento):
    conexao = connect()
    conexao.execute('INSERT INTO Multa(id_emprestimo, valor, status_pagamento) VALUES (?, ?, ?)',\
                    (id_emprestimo, valor, status_pagamento))
    conexao.commit()
    conexao.close()

#Função para visualizar Multas
def get_fines():
    conexao = connect()
    c = conexao.cursor()
    c.execute('SELECT * FROM Multa')
    multas = c.fetchall()
    conexao.close()
    return multas

#Função para atualizar as Multas
def update_fines_status(id_multa, status_pagamento):
    conexao = connect()
    conexao.execute('UPDATE Multa SET status_pagamento = ? WHERE id_multa = ?',\
                    (status_pagamento, id_multa))
    conexao.commit()
    conexao.close()

#Função para a tabela de Categoria
def insert_category(nome):
    conexao = connect()
    conexao.execute('INSERT INTO Categoria(nome) VALUES (?)', (nome))
    conexao.commit()
    conexao.close()

#Função para Exibir as Categorias
def get_categories():
    conexao = connect()
    c = conexao.cursor()
    c.execute('SELECT * FROM Categoria')
    categorias = c.fetchall()
    conexao.close()
    return categorias

#Função para atualizar Categorias
def update_category(id_categoria, nome):
    conexao = connect()
    conexao.execute('UPDATE Categoria SET nome = ? WHERE id_categoria = ?',
                    (nome, id_categoria))
    conexao.commit()
    conexao.close()