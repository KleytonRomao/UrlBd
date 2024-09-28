import sqlite3
import argparse

### Banco de Dados 
def bds(titulo, url ,conteudo):
    con = sqlite3.connect("tarefas.db")
    cur = con.cursor()
    cur.execute('''INSERT INTO tarefas (titulo, url, conteudo) VALUES (?, ?, ?)''', (titulo, url, conteudo))
    con.commit()
    con.close()

### Busca
def busca(id):
    con = sqlite3.connect("tarefas.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
    resultado = cur.fetchall()
    if resultado:
        for line in resultado:
            print(f'Título: {line[1]}\nUrl: {line[2]}\nConteudo: {line[3]}')
    else:
        print("Nenhuma tarefa encontrada com esse ID.")
    con.close()

## Listar tarefas cadastradas 
def cadastrados():
    con = sqlite3.connect("tarefas.db")
    cur = con.cursor()
    cur.execute('''SELECT * FROM tarefas;''')
    tarefas = cur.fetchall()
    con.close()
    print("Seus títulos:\n")
    for tarefa in tarefas:
        print(f'{tarefa[0]} - {tarefa[1]}')
    print()

## Criar tabela se não existir 
def criar_tabela():
    con = sqlite3.connect("tarefas.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    url TEXT NOT NULL,
                    conteudo TEXT NOT NULL)''')
    con.commit()
    con.close()

def main():
    # Criar parser de argumentos
    parser = argparse.ArgumentParser(description='Gerenciador de Url.')
    subparsers = parser.add_subparsers(dest='comando')

    # Subcomando para adicionar tarefa
    parser_add = subparsers.add_parser('ad', help='Adicionar uma nova Url')
    
    # Subcomando para buscar tarefa por ID
    parser_busca = subparsers.add_parser('b', help='Buscar Url por ID')
    parser_busca.add_argument('id', type=int, help='ID da Url')

    # Subcomando para listar tarefas
    parser_listar = subparsers.add_parser('l', help='Listar todas as urls cadastradas')

    # Analisar os argumentos
    args = parser.parse_args()

    # Executar o comando correspondente
    if args.comando == 'ad':
        titulo = input("Digite o titulo ")
        url = input("Digite a Url ")
        conteudo = input("Digite o conteudo ")
        bds(titulo,url, conteudo)
        print(f'Tarefa adicionada')
    elif args.comando == 'b':
        busca(args.id)
    elif args.comando == 'l':
        cadastrados()
    else:
        parser.print_help()

if __name__ == "__main__":
    criar_tabela()  # Criar a tabela, se não existir
    main()          # Iniciar a interface

