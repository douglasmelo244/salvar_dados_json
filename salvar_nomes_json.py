import json

Documento = 'documento.json'

class Preparo:
    def __init__(self):
        self.lista = []
        
        try:
            self.importar_dados()
        except FileNotFoundError:
            print('Não há dados armazenados atualmente.')
        except json.JSONDecodeError:
            print('Erro ao ler o arquivo de dados. O arquivo pode estar corrompido.')

    def fazer_dump(self):
        with open(Documento, 'w', encoding='utf-8') as arquivo:
            json.dump(self.lista, arquivo, ensure_ascii=False, indent=2)

    def importar_dados(self):
        with open(Documento, 'r', encoding='utf-8') as arquivo:
            self.lista = json.load(arquivo)

class AcoesUsuario(Preparo):
    def __init__(self):
        super().__init__()

    def adicionar(self):
        nome = input('Qual o nome? ')
        idade = input('Qual a idade? ')
        
        dados = {
            'Nome': nome,
            'Idade': idade,
        }
        self.lista.append(dados)
        self.fazer_dump()
        print('Tarefa adicionada com sucesso!')
        print('-' * 20)

    def listar(self):
        if not self.lista:
            print('A lista está vazia.')
            print('-' * 20)
            return
        
        for indice, item in enumerate(self.lista):
            print(f'{indice} - Nome: {item["Nome"]}, Idade: {item["Idade"]}')
        print('-' * 20)

    def deletar(self):
        self.listar()
        if not self.lista:
            return
        
        try:
            indice = int(input("Digite o número do índice do item a ser deletado: "))
            if 0 <= indice < len(self.lista):
                del self.lista[indice]
                self.fazer_dump()
                print('Item deletado com sucesso!')
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")
        print('-' * 20)

    def opcoes(self):
        while True:
            print('A - Adicionar item\nB - Listar\nC - Atualizar\nD - Deletar\nE - Sair')
            opcao = input('Qual a opção desejada? ').upper()
            print('-' * 20)
            if opcao == 'A':
                self.adicionar()
            elif opcao == 'B':
                self.listar()
            elif opcao == 'C':
                self.atualizar()
            elif opcao == 'D':
                self.deletar()
            elif opcao == 'E':
                print('Encerrando o programa.')
                break
            else:
                print('Opção inválida.')
                print('-' * 20)

    def atualizar(self):
        self.listar()
        if not self.lista:
            return
        
        try:
            indice = int(input("Digite o número do índice do item a ser atualizado: "))
            if 0 <= indice < len(self.lista):
                nome = input('Novo nome: ')
                idade = input('Nova idade: ')
                self.lista[indice] = {'Nome': nome, 'Idade': idade}
                self.fazer_dump()
                print('Item atualizado com sucesso!')
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")
        print('-' * 20)

tarefas = AcoesUsuario()
tarefas.opcoes()
