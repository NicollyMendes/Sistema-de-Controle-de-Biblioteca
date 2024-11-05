import sqlite3


conexao = sqlite3.connect('dados_biblioteca.db')


#LIVROS
conexao.execute('''CREATE TABLE Livros(
                   id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT,
                   autor TEXT,
                   editora TEXT,
                   isbn TEXT,
                   ano_de_publicacao INTEGER,
                   genero TEXT,
                   quantidade_disponivel INTEGER)''')

#USUARIOS
conexao.execute('''CREATE TABLE Usuarios(
                   id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   sobrenome TEXT,
                   endereco TEXT,
                   email TEXT,
                   telefone TEXT)''')

#Empréstimos
conexao.execute('''CREATE TABLE Emprestimos(
                   id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
                   id_livro INTEGER,
                   id_usuario INTEGER,
                   data_emprestimo DATE,
                   data_devolucao_prevista DATE,
                   data_devolucao_real DATE,
                   status TEXT,
                   FOREIGN KEY(id_livro) REFERENCES Livros(id_livro),
                   FOREIGN KEY(id_usuario) REFERENCES Usuarios(id_usuario))''')
    
#Reservas
conexao.execute('''CREATE TABLE Reservas(
                   id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
                   id_usuario INTEGER,
                   id_livro INTEGER,
                   data_reserva DATE,
                   status_reserva TEXT,
                   FOREIGN KEY(id_usuario) REFERENCES Usuarios(id_usuario),
                   FOREIGN KEY(id_livro) REFERENCES Livros(id_livro))''')
    
#Multas
conexao.execute('''CREATE TABLE Multa(
                   id_multa INTEGER PRIMARY KEY AUTOINCREMENT,
                   id_emprestimo INTEGER,
                   valor FLOAT,
                   status_pagamento TEXT,
                   FOREIGN KEY(id_emprestimo) REFERENCES Emprestimos(id_emprestimo))''')
    
#Categoria
conexao.execute('''CREATE TABLE Categoria(
                   id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT)''')