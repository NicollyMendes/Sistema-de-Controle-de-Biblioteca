# Sistema de Controle de Biblioteca

Um sistema de gerenciamento para bibliotecas que facilita o cadastro e gerenciamento de livros, usuários, empréstimos, devoluções, reservas e multas. O sistema foi desenvolvido com uma interface gráfica utilizando Tkinter em Python
e integra-se com um banco de dados SQLite para armazenamento de dados.

## Índice
- [Recursos](#recursos)
- [Pré-Requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#comousar)
- [Estrutura do Projeto](#estruturadoprojeto)
- [Contribução](#contribuição)
- [Licença](#licença)

## Recursos
O sistema oferece funcionalidades completas para a gestão de uma biblioteca:
- **Cadastro e visualização de livros e usuários**
- **Empréstimo e devolução de livros**
- **Consulta de livros e usuários cadastrados**
- **Inserção e visualização de multas por atraso**
- **Reserva de livros**
- **Interface intuitiva e menus de navegação**
- **Busca de livros por título, autor, editora, ano de publicação ou gênero**

## Pré-Requisitos
Para rodas o sistema, você precisará de:
- Python 3.8 ou superior
- Biblioteca Pillow para manipulação de imagens
- Tkinter (já incluido no Python)
- -SQLite3 para banco de dados (já incluido no Python)

## Instalação
1. **Clone o repositório para o seu ambiente local**:
   ```bash
   git clone https://github.com/NicollyMendes/Sistema-de-Controle-de-Biblioteca.git
2. **Acesse o diretório do Projeto**:
   ```bash
   cd Sistema-de-Controle-de-Biblioteca
3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt

## Como Usar
1. **Execute o Sistema**:
   ```bash
   python sys.py
2. **Navegue pelo menu do lado esquerdo para acessar as funcionalidades**:
 - Novo Usuário: Cadastrar um novo usuário na biblioteca.
 - Novo Livro: Registar um novo livro.
 - Realizar Empréstimo: Registrar um empréstimo para um usuário.
 - Devolução de Empréstimo: Registrar a devolução de um empréstimo.
 - Inserir Multa: Aplicar uma multa para empréstimos em atraso.
 - Reserva de Livro: Registrar uma reserva para um livro.

3. **O sistema exibirá informações detalhadas e formulários de preenchimento em cada seção.**

## Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.


