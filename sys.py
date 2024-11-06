from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Style
from PIL import Image, ImageTk
from datetime import datetime
from datetime import *
from view import *

# INTERFACE GRÁFICA
# Criando janela ------
janela = Tk()
janela.title('Sistema de Gerenciamento de Livros')
janela.geometry('900x530')
janela.configure(background='#DAD7CD')
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

# Frames ------
frameCima = Frame(janela, width=990, height=50, background='#A3B18A', relief='flat')
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsq = Frame(janela, width=150, height=450, background='#588157', relief='solid')
frameEsq.grid(row=1, column=0, sticky=NSEW)

frameDir = Frame(janela, width=600, height=450, background='#DAD7CD', relief='raised')
frameDir.grid(row=1, column=1, sticky=NSEW)

# Logo ----------
app_img = Image.open('Sistema-de-Controle-de-Biblioteca/iconelivro.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, anchor=NW, bg='#A3B18A', fg='#344E41')
app_logo.place(x=5, y=0)

app_title = Label(frameCima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg='#A3B18A', fg='#344E41')
app_title.place(x=50, y=7)

app_linha = Label(frameCima, width=900, height=1, padx=5, anchor=NW, font=('Verdana 1'), bg='#344E41', fg='#DAD7CD')
app_linha.place(x=0, y=47)

# Função para cadastro de novo Livro
def novo_livro():
    global img_salvar

    def add():
        titulo = e_titulo.get()
        autor = e_autor.get()
        editora = e_editora.get()
        isbn = e_isbn.get()
        ano_de_publicacao = e_ano_de_publicacao.get()
        genero = combo_genero.get()
        quantidade_disponivel = combo_quantidade_disponivel.get()

        lista = [titulo, autor, editora, isbn, ano_de_publicacao, genero, quantidade_disponivel]

        for campo in lista:
            if campo == '':
                messagebox.showerror('ERRO', 'Preencha todos os campos!')
                return
        insert_book(titulo, autor, editora, isbn, ano_de_publicacao, genero, quantidade_disponivel)
        messagebox.showinfo('Sucesso', 'Livro cadastrado com sucesso!')

        e_titulo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_isbn.delete(0, END)
        e_ano_de_publicacao.delete(0, END)
        combo_genero.set('')
        combo_quantidade_disponivel.set('')

    # Limpa o frame para exibir os campos corretamente
    for widget in frameDir.winfo_children():
        widget.destroy()

    # Configuração de Interface para Novo Livro
    app_ = Label(frameDir, text='Inserir um Novo Livro', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    l_titulo = Label(frameDir, text='Título', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_titulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_titulo = Entry(frameDir, width=25, justify='left', relief='solid')
    e_titulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_autor = Label(frameDir, text='Autor', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameDir, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_editora = Label(frameDir, text='Editora', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameDir, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_isbn = Label(frameDir, text='ISBN', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_isbn.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn = Entry(frameDir, width=25, justify='left', relief='solid')
    e_isbn.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_ano_de_publicacao = Label(frameDir, text='Ano de Publicação', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_ano_de_publicacao.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano_de_publicacao = Entry(frameDir, width=25, justify='left', relief='solid')
    e_ano_de_publicacao.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    l_genero = Label(frameDir, text='Gênero', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_genero.grid(row=7, column=0, padx=5, pady=5, sticky=NSEW)
    combo_genero = Combobox(frameDir, state='readonly')
    combo_genero['values'] = ['Ficção Científica', 'Fantasia', 'Romance', 'Suspense', 'Thriller', 'Horror', 'Drama', 'Aventura']
    combo_genero.grid(row=7, column=1, padx=5, pady=5, sticky=NSEW)

    l_quantidade_disponivel = Label(frameDir, text='Quantidade Disponível', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_quantidade_disponivel.grid(row=8, column=0, padx=5, pady=5, sticky=NSEW)
    combo_quantidade_disponivel = Combobox(frameDir, state='readonly')
    combo_quantidade_disponivel['values'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    combo_quantidade_disponivel.grid(row=8, column=1, padx=5, pady=5, sticky=NSEW)

    img_salvar = Image.open('Sistema-de-Controle-de-Biblioteca/salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='Salvar', bg='#588157', fg='#DAD7CD', font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=9, column=1, pady=5, sticky=NSEW)

# Função para visualizar todos os livros
def ver_livros():
    app_ = Label(frameDir, text='Todos os Livros', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, pady=(5,5), sticky="ew")

    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1'), bg='#344E41', fg='#DAD7CD')
    app_linha.grid(row=1, column=0, columnspan=4, sticky="ew")

    dados = get_books()  # Supondo que get_books retorne uma lista de livros

    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano de Publicação', 'ISBN', 'Qnt. Disp']

    global tree
    tree = Treeview(frameDir, selectmode='extended', columns=list_header, show='headings')

    vsb = Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 165, 110, 100, 50, 50, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for livro in dados:
        tree.insert('', 'end', values=livro)

# Função para buscar livros por filtros
def buscar_livro():
    global tree  # Coloque a declaração global aqui no início da função

    # Limpa o frame para exibir os campos corretamente
    for widget in frameDir.winfo_children():
        widget.destroy()

    def realizar_busca():
        # Obtém os valores dos campos de entrada
        titulo = e_titulo.get().strip()
        autor = e_autor.get().strip()
        editora = e_editora.get().strip()
        ano_de_publicacao = e_ano_de_publicacao.get().strip()
        genero = combo_genero.get().strip()

        # Chama a função search_books com os parâmetros informados
        resultados = search_books(
            titulo=titulo if titulo else None,
            autor=autor if autor else None,
            editora=editora if editora else None,
            ano_de_publicacao=int(ano_de_publicacao) if ano_de_publicacao else None,
            genero=genero if genero else None
        )

        # Limpa os resultados anteriores na Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Insere os novos resultados
        for livro in resultados:
            tree.insert('', 'end', values=livro)

    # Título da seção
    app_ = Label(frameDir, text='Buscar Livro', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    # Campos de entrada para filtros de busca
    l_titulo = Label(frameDir, text='Título', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_titulo.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)
    e_titulo = Entry(frameDir, width=25, justify='left', relief='solid')
    e_titulo.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    l_autor = Label(frameDir, text='Autor', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_autor.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameDir, width=25, justify='left', relief='solid')
    e_autor.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_editora = Label(frameDir, text='Editora', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_editora.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameDir, width=25, justify='left', relief='solid')
    e_editora.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_ano_de_publicacao = Label(frameDir, text='Ano de Publicação', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_ano_de_publicacao.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano_de_publicacao = Entry(frameDir, width=25, justify='left', relief='solid')
    e_ano_de_publicacao.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_genero = Label(frameDir, text='Gênero', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_genero.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    combo_genero = Combobox(frameDir, state='readonly')
    combo_genero['values'] = ['Ficção Científica', 'Fantasia', 'Romance', 'Suspense', 'Thriller', 'Horror', 'Drama', 'Aventura']
    combo_genero.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    # Botão para realizar a busca
    b_buscar = Button(frameDir, command=realizar_busca, text='Buscar', bg='#588157', fg='#DAD7CD', font=('Ivy 10'), overrelief=RIDGE, relief=GROOVE)
    b_buscar.grid(row=6, column=1, pady=10, sticky=NSEW)

    # Configuração da Treeview para exibir os resultados
    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano de Publicação', 'ISBN', 'Gênero']

    tree = Treeview(frameDir, selectmode='extended', columns=list_header, show='headings')

    vsb = Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=7, columnspan=4, sticky='nsew')
    vsb.grid(column=4, row=7, sticky='ns')
    hsb.grid(column=0, row=8, columnspan=4, sticky='ew')

    hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
    h = [30, 150, 100, 100, 80, 80, 80]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1
# Adiciona a opção no menu para buscar livros
img_buscar = Image.open('Sistema-de-Controle-de-Biblioteca/buscaricon.png')
img_buscar = img_buscar.resize((18, 18))
img_buscar = ImageTk.PhotoImage(img_buscar)
b_buscar_livro = Button(frameEsq, command=lambda: control('buscar_livro'), image=img_buscar, compound=LEFT, anchor=NW, text=' Buscar Livro', bg='#588157', fg='#DAD7CD', font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_buscar_livro.grid(row=11, column=0, sticky=NSEW, padx=5, pady=6)    

# Função para adicionar um novo usuário
def novo_usuario():
    global img_salvar

    def add():
        p_nome = e_p_nome.get()
        sobrenome = e_sobrenome.get()
        endereco = e_endereco.get()
        email = e_email.get()
        telefone = e_telefone.get()

        lista = [p_nome, sobrenome, endereco, email, telefone]

        for i in lista:
            if i == '':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return
            
        insert_user(p_nome, sobrenome, endereco, email, telefone)
        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso.')
        e_p_nome.delete(0, END)
        e_sobrenome.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)

    # Limpa o frame para exibir os campos corretamente
    for widget in frameDir.winfo_children():
        widget.destroy()

    # Configurações da Interface para Novo Usuário
    app_ = Label(frameDir, text='Inserir um novo usuário', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    l_p_nome = Label(frameDir, text='Primeiro Nome*', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_nome = Entry(frameDir, width=25, justify='left', relief='solid')
    e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_sobrenome = Label(frameDir, text='Sobrenome*', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_sobrenome = Entry(frameDir, width=25, justify='left', relief='solid')
    e_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_endereco = Label(frameDir, text='Endereço do usuário*', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_endereco = Entry(frameDir, width=25, justify='left', relief='solid')
    e_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_email = Label(frameDir, text='Endereço de e-mail*', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_email = Entry(frameDir, width=25, justify='left', relief='solid')
    e_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_telefone = Label(frameDir, text='Número de telefone*', anchor=NW, font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_telefone.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_telefone = Entry(frameDir, width=25, justify='left', relief='solid')
    e_telefone.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    img_salvar = Image.open('Sistema-de-Controle-de-Biblioteca/salvaricon.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDir, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='Salvar', bg='#588157', fg='#DAD7CD', font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Ver usuarios
def ver_usuarios():
    app_ = Label(frameDir, text='Ver Usuários', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4,pady=(5,5), sticky="ew")

    app_linha = Label(frameDir, width=400, height=1, anchor=NW, font=('Verdana 1'), bg='#344E41', fg='#DAD7CD')
    app_linha.grid(row=1, column=0, columnspan=4, sticky="ew")

    dados = get_users()

    list_header = ['ID', 'Nome', 'Sobrenome', 'Endereço', 'Email', 'Telefone']

    global tree
    tree = Treeview(frameDir, selectmode='extended', columns=list_header, show='headings')

    vsb = Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDir.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 100, 100, 150, 120, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

# Função para realizar empréstimo
def realizar_emprestimo():
    # Obter todos os usuários e livros para as comboboxes
    usuarios = get_users()  # Supondo que get_users retorna [(ID, Nome), ...]
    livros = get_books()    # Supondo que get_books retorna [(ID, Título), ...]

    # Função para adicionar empréstimo
    def add():
        usuario_info = combo_usuario.get()
        livro_info = combo_livro.get()
        data_emprestimo = datetime.now().strftime('%Y-%m-%d')
        data_devolucao_prevista = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        status = 'Ativo'

        # Extrair o ID do usuário e do livro das strings selecionadas
        usuario_id = usuario_info.split(" - ")[0] if usuario_info else ""
        livro_id = livro_info.split(" - ")[0] if livro_info else ""

        if usuario_id == '' or livro_id == '':
            messagebox.showerror('Erro', 'Selecione um usuário e um livro.')
            return

        insert_loan(usuario_id, livro_id, data_emprestimo,data_devolucao_prevista, status)
        messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso.')

        combo_usuario.set('')
        combo_livro.set('')

    # Configurações da Interface
    app_ = Label(frameDir, text='Realizar um Empréstimo', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    l_usuario = Label(frameDir, text='Usuário', font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_usuario.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)
    
    combo_usuario = Combobox(frameDir, state='readonly', width=25)
    combo_usuario['values'] = [f"{user[0]} - {user[1]}" for user in usuarios]  # Formato "ID - Nome"
    combo_usuario.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    l_livro = Label(frameDir, text='Livro', font=('Ivy 10'), bg='#DAD7CD', fg='#3A5A40')
    l_livro.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    
    combo_livro = Combobox(frameDir, state='readonly', width=25)
    combo_livro['values'] = [f"{livro[0]} - {livro[1]}" for livro in livros]  # Formato "ID - Título"
    combo_livro.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    b_salvar = Button(frameDir, command=add, text='Salvar', bg='#588157', fg='#DAD7CD', font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=3, column=1, pady=5, sticky=NSEW)

def ver_livros_emprestados():
    # Limpa o frame antes de exibir o conteúdo
    for widget in frameDir.winfo_children():
        widget.destroy()

    # Configuração do cabeçalho
    app_ = Label(frameDir, text='Livros Emprestados', font=('Verdana 10 bold'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, pady=(5, 5), sticky="ew")

    # Obtém os dados dos empréstimos
    dados = get_books_loan()  # Certifique-se de que get_books_loan() retorna uma lista de tuplas [(ID Empréstimo, ID Livro, Nome Usuário, Data Empréstimo, Data Devolução), ...]

    # Verifica se há dados para exibir
    if not dados:
        messagebox.showinfo("Informação", "Nenhum livro emprestado no momento.")
        return

    # Configuração da tabela
    list_header = ['ID Empréstimo', 'ID Livro', 'Nome Usuário', 'Data Empréstimo', 'Data Devolução']

    global tree
    tree = Treeview(frameDir, selectmode="extended", columns=list_header, show="headings")

    vsb = Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')

    # Configurações de cabeçalho e largura das colunas
    hd = ["nw", "nw", "nw", "nw", "nw"]
    h = [20, 150, 150, 100, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # Insere os dados na tabela
    for item in dados:
        tree.insert('', 'end', values=item)

    # Ajusta o layout do frame
    frameDir.grid_rowconfigure(0, weight=1)
# Função para devolução de um empréstimo
def devolucao_emprestimo():
    # Limpa o frame direito antes de inserir novos widgets
    for widget in frameDir.winfo_children():
        widget.destroy()

    # Função que será chamada ao clicar no botão de registrar devolução
    def add():
        emprestimo_selecionado = combo_emprestimo.get()
        if not emprestimo_selecionado:
            messagebox.showerror('Erro', 'Selecione um empréstimo')
            return

        emprestimo_id = emprestimo_selecionado.split(" - ")[0]  # Extrai o ID do empréstimo
        data_devolucao_real = datetime.now().strftime('%Y-%m-%d')

        # Função que registra a devolução (certifique-se de que está implementada corretamente)
        update_loan_return_date(emprestimo_id, data_devolucao_real)
        messagebox.showinfo('Sucesso', 'Devolução registrada com sucesso.')
        combo_emprestimo.set('')  # Limpa a seleção

    # Obtém os empréstimos no formato [(ID, Título Livro, Nome Usuário, Data Empréstimo, Data Devolução), ...]
    try:
        emprestimos = get_books_loan()  # Certifique-se de que esta função está definida e retorna os dados corretamente
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao buscar empréstimos: {e}')
        return

    # Verifica se há empréstimos para exibir na combobox
    if not emprestimos:
        messagebox.showinfo('Informação', 'Não há empréstimos registrados para devolução.')
        return

    # Formata os empréstimos para exibir no combobox
    emprestimo_opcoes = [f"{item[0]} - {item[1]} - {item[2]}" for item in emprestimos]

    # Configura a interface da seção de devolução de empréstimos
    Label(frameDir, text='Registrar Devolução de Empréstimo', font=('Verdana 10 bold'), bg='#DAD7CD').grid(row=0, column=0, columnspan=2, pady=5)
    
    Label(frameDir, text='Empréstimo:', bg='#DAD7CD').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    combo_emprestimo = Combobox(frameDir, values=emprestimo_opcoes, state='readonly', width=50)
    combo_emprestimo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    Button(frameDir, text='Registrar', command=add, width=20, bg='#588157', fg='#DAD7CD').grid(row=2, column=1, padx=5, pady=10, sticky=W)
# Função para adicionar uma reserva
def adicionar_reserva():
    # Limpa o frame direito antes de inserir novos widgets
    for widget in frameDir.winfo_children():
        widget.destroy()

    # Função que será chamada ao clicar no botão para registrar a reserva
    def add():
        usuario_info = combo_usuario.get()
        livro_info = combo_livro.get()
        data_reserva = datetime.now().strftime('%Y-%m-%d')
        status_reserva = combo_status_reserva.get()

        # Extrair ID do usuário e ID do livro das strings selecionadas
        usuario_id = usuario_info.split(" - ")[0] if usuario_info else ""
        livro_id = livro_info.split(" - ")[0] if livro_info else ""

        if not (usuario_id and livro_id and status_reserva):
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

        # Insere a reserva no banco de dados
        insert_reservation(usuario_id, livro_id, data_reserva, status_reserva)
        messagebox.showinfo('Sucesso', 'Reserva adicionada com sucesso!')
        combo_usuario.set('')
        combo_livro.set('')
        combo_status_reserva.set('')

    # Obtenha todos os usuários e livros para as comboboxes
    usuarios = get_users()  # [(ID, Nome), ...]
    livros = get_books()    # [(ID, Título), ...]

    # Verifica se há usuários e livros para exibir na combobox
    if not usuarios or not livros:
        messagebox.showerror("Erro", "Usuários ou livros não encontrados.")
        return

    # Formata as opções para as comboboxes
    usuario_opcoes = [f"{id_usuario} - {nome}" for id_usuario, nome, *_ in usuarios]
    livro_opcoes = [f"{id_livro} - {titulo}" for id_livro, titulo, *_  in livros]

    # Interface para adicionar reserva
    Label(frameDir, text="Adicionar Nova Reserva", font=('Verdana 10 bold'), bg='#DAD7CD').grid(row=0, column=0, columnspan=2, pady=5)

    Label(frameDir, text="Usuário:", bg='#DAD7CD').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    combo_usuario = Combobox(frameDir, values=usuario_opcoes, state='readonly', width=50)
    combo_usuario.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    Label(frameDir, text="Livro:", bg='#DAD7CD').grid(row=2, column=0, padx=5, pady=5, sticky=W)
    combo_livro = Combobox(frameDir, values=livro_opcoes, state='readonly', width=50)
    combo_livro.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    Label(frameDir, text="Status da Reserva:", bg='#DAD7CD').grid(row=3, column=0, padx=5, pady=5, sticky=W)
    combo_status_reserva = Combobox(frameDir, values=['Pendente', 'Concluída', 'Cancelada'], state='readonly', width=47)
    combo_status_reserva.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    Button(frameDir, text="Salvar Reserva", command=add, width=20, bg='#588157', fg='#DAD7CD').grid(row=4, column=1, padx=5, pady=15, sticky=W)

# Função para visualizar reservas
def visualizar_reserva():
    app_ = Label(frameDir, text='Visualizar Reservas', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    dados = get_reservations()

    list_header = ['ID Reserva', 'ID Usuário', 'ID Livro', 'Data Reserva', 'Status']

    global tree
    tree = Treeview(frameDir, columns=list_header, show='headings')

    vsb = Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, columnspan=2, sticky='ew')

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=120, anchor='nw')

    for reserva in dados:
        tree.insert('', 'end', values=reserva)

    tree.bind("<Double-1>", atualizar_reserva_com_duplo_clique)

# Função para atualizar reserva com duplo clique
def atualizar_reserva_com_duplo_clique(event):
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showerror("Erro", "Nenhuma reserva selecionada.")
        return

    reserva_id = tree.item(item_selecionado, 'values')[0]
    status_atual = tree.item(item_selecionado, 'values')[4]
    novo_status = "Concluída" if status_atual == "Pendente" else "Pendente"

    update_reservation_status(reserva_id, novo_status)

    tree.item(item_selecionado, values=(tree.item(item_selecionado, 'values')[:4] + (novo_status,)))

# Função para inserir uma multa com cálculo automático
def inserir_multa():
    # Limpa o frame direito antes de inserir novos widgets
    for widget in frameDir.winfo_children():
        widget.destroy()

    # Função que será chamada ao clicar no botão de registrar multa
    def add():
        emprestimo_selecionado = combo_emprestimo.get()
        if not emprestimo_selecionado:
            messagebox.showerror('Erro', 'Selecione um empréstimo')
            return

        emprestimo_id = emprestimo_selecionado.split(" - ")[0]  # Extrai o ID do empréstimo
        valor_diario_multa = 2.00  # Defina o valor diário da multa

        # Tenta buscar a data de vencimento e devolução do empréstimo
        try:
            data_vencimento = get_loan_due_date(emprestimo_id)
            data_devolucao = get_loan_return_date(emprestimo_id)
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao buscar dados do empréstimo: {e}')
            return

        # Calcula os dias de atraso
        if data_devolucao is None:
            messagebox.showerror('ERRO', 'Empréstimo ainda não foi devolvido, não é possível calcular multa.')
            return

        dias_atraso = (data_devolucao - data_vencimento).days
        valor_multa = max(0, dias_atraso * valor_diario_multa)

        # Insere a multa no banco de dados
        insert_fine(emprestimo_id, valor_multa)
        messagebox.showinfo('Sucesso', f'Multa de R${valor_multa:.2f} inserida com sucesso')

        combo_emprestimo.set('')  # Limpa a seleção

    # Obtém os empréstimos no formato [(ID, Título Livro, Nome Usuário), ...]
    try:
        emprestimos = get_books_loan()  # Certifique-se de que esta função está definida e retorna os dados corretamente
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao buscar empréstimos: {e}')
        return

    # Verifica se há empréstimos para exibir na combobox
    if not emprestimos:
        messagebox.showinfo('Informação', 'Não há empréstimos registrados para cálculo de multa.')
        return

    # Formata os empréstimos para exibir no combobox
    emprestimo_opcoes = [f"{id} - {livro} - {usuario}" for id, livro, usuario in emprestimos]

    # Configura a interface da seção de inserção de multas
    Label(frameDir, text='Inserir Multa', font=('Verdana 10 bold'), bg='#DAD7CD').grid(row=0, column=0, columnspan=2, pady=5)
    
    Label(frameDir, text='Empréstimo:', bg='#DAD7CD').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    combo_emprestimo = Combobox(frameDir, values=emprestimo_opcoes, state='readonly', width=50)
    combo_emprestimo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    Button(frameDir, text='Registrar Multa', command=add, width=20, bg='#588157', fg='#DAD7CD').grid(row=2, column=1, padx=5, pady=10, sticky=W)

# Função para visualizar multas
def visualizar_multas():
    app_ = Label(frameDir, text='Visualizar Multas', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg='#DAD7CD', fg='#3A5A40')
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    dados = get_fines()

    list_header = ['ID Multa', 'ID Empréstimo', 'Valor Multa', 'Data Multa']

    global tree
    tree = Treeview(frameDir, columns=list_header, show='headings')

    vsb = Scrollbar(frameDir, orient='vertical', command=tree.yview)
    hsb = Scrollbar(frameDir, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, columnspan=2, sticky='ew')

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=120, anchor='nw')

    for multa in dados:
        tree.insert('', 'end', values=multa)

#Função para controlar o Menu
def control(i):
    for widget in frameDir.winfo_children():
       widget.destroy()

    if i == 'novo_usuario':
        novo_usuario()

    elif i == 'ver_usuarios':
       ver_usuarios()

    elif i == 'novo_livro':
       novo_livro()

    elif i == 'ver_livros':
       ver_livros()

    elif i == 'buscar_livro':
        buscar_livro() 

    elif i == 'realizar_emprestimo':
       realizar_emprestimo()

    elif i == 'ver_livros_emprestados':
       ver_livros_emprestados()

    elif i == 'devolucao_emprestimo':
       devolucao_emprestimo()

    elif i == 'adicionar_reserva':
       adicionar_reserva()

    elif i == 'visualizar_reserva':
       visualizar_reserva()
    
    elif i == 'inserir_multa':
       inserir_multa()
    
    elif i == 'visualizar_multas':
       visualizar_multas()
#MENU ------
#NOVO USUARIO
# Novo user
img_usuario = Image.open('Sistema-de-Controle-de-Biblioteca/addicon.png')
img_usuario = img_usuario.resize((18, 18))
img_usuario = ImageTk.PhotoImage(img_usuario)
#criando botao do novo usuário
b_usuario = Button(frameEsq, command=lambda:control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text=' Novo usuário', bg='#588157', fg='#DAD7CD',
                   font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo livro
img_novo_livro = Image.open('Sistema-de-Controle-de-Biblioteca/addicon.png')
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
#criando botao do novo livro
b_novo_livro = Button(frameEsq, command=lambda:control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text=' Novo livro', bg='#588157', fg='#DAD7CD',
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver livros
img_ver_livro = Image.open('Sistema-de-Controle-de-Biblioteca/iconelivro.png')
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
#criando botao de ver os livros
b_ver_livro = Button(frameEsq, command=lambda:control('ver_livros'), image=img_ver_livro, compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg='#588157', fg='#DAD7CD',
                     font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Ver todos usuarios
img_ver_usuario = Image.open('Sistema-de-Controle-de-Biblioteca/usericon.png')
img_ver_usuario = img_ver_usuario.resize((18, 18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
#criando botao de ver os usuarios
b_ver_usuario = Button(frameEsq, command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text=' Exibir todos os usuários', bg='#588157', fg='#DAD7CD',
                       font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar emprestimo
img_emprestimo = Image.open('Sistema-de-Controle-de-Biblioteca/addicon.png')
img_emprestimo = img_emprestimo.resize((18, 18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
#criando botao de realizar emprestimo
b_emprestimo = Button(frameEsq, command=lambda:control('realizar_emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text=' Realizar um empréstimo', bg='#588157', fg='#DAD7CD',
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolucao do Emprestimo
img_dev_emprestimo = Image.open('Sistema-de-Controle-de-Biblioteca/updateicon.png')
img_dev_emprestimo = img_dev_emprestimo.resize((18, 18))
img_dev_emprestimo = ImageTk.PhotoImage(img_dev_emprestimo)
#criando botao de devolucao de emprestimo
b_dev_emprestimo = Button(frameEsq, command=lambda:control('devolucao_emprestimo'), image=img_dev_emprestimo, compound=LEFT, anchor=NW, text=' Devolução de um empréstimo', bg='#588157', fg='#DAD7CD',
                          font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_dev_emprestimo.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Ver livros emprestados
img_ver_emprestimo = Image.open('Sistema-de-Controle-de-Biblioteca/carrinhoicon.png')
img_ver_emprestimo = img_ver_emprestimo.resize((18, 18))
img_ver_emprestimo = ImageTk.PhotoImage(img_ver_emprestimo)
#criando botao de ver os livros emprestados
b_ver_emprestimo = Button(frameEsq, command=lambda:control('ver_livros_emprestados'), image=img_ver_emprestimo, compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg='#588157', fg='#DAD7CD',
                          font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_emprestimo.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

# Adicionar reserva
img_reserva = Image.open('Sistema-de-Controle-de-Biblioteca/addicon.png')
img_reserva = img_reserva.resize((18, 18))
img_reserva = ImageTk.PhotoImage(img_reserva)
#criando botao de realizar reserva
b_reserva = Button(frameEsq, command=lambda:control('adicionar_reserva'), image=img_reserva, compound=LEFT, anchor=NW, text=' Realizar uma reserva', bg='#588157', fg='#DAD7CD',
                   font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_reserva.grid(row=7, column=0, sticky=NSEW, padx=5, pady=6)

# Ver reservas
img_ver_reserva = Image.open('Sistema-de-Controle-de-Biblioteca/carrinhoicon.png')
img_ver_reserva = img_ver_reserva.resize((18, 18))
img_ver_reserva = ImageTk.PhotoImage(img_ver_reserva)
#criando botao de ver as reservas
b_ver_reserva = Button(frameEsq, command=lambda:control('visualizar_reserva'), image=img_ver_reserva, compound=LEFT, anchor=NW, text=' Exibir todas as reservas', bg='#588157', fg='#DAD7CD',
                       font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_reserva.grid(row=8, column=0, sticky=NSEW, padx=5, pady=6)

# Adicionar multa
img_multa = Image.open('Sistema-de-Controle-de-Biblioteca/addicon.png')
img_multa = img_multa.resize((18, 18))
img_multa = ImageTk.PhotoImage(img_multa)
#criando botao de adicionar multa
b_multa = Button(frameEsq, command=lambda:control('inserir_multa'), image=img_multa, compound=LEFT, anchor=NW, text=' Inserir multa', bg='#588157', fg='#DAD7CD',
                 font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_multa.grid(row=9, column=0, sticky=NSEW, padx=5, pady=6)

# Ver multas
img_ver_multas = Image.open('Sistema-de-Controle-de-Biblioteca/multaicone.png')
img_ver_multas = img_ver_multas.resize((18, 18))
img_ver_multas = ImageTk.PhotoImage(img_ver_multas)
#criando botao de ver multas
b_ver_multas = Button(frameEsq, command=lambda:control('visualizar_multas'), image=img_ver_multas, compound=LEFT, anchor=NW, text=' Visualizar multas', bg='#588157', fg='#DAD7CD',
                      font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_multas.grid(row=10, column=0, sticky=NSEW, padx=5, pady=6)

janela.mainloop()