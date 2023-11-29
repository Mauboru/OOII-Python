from model.daos.Conexao import Conexao
from model.daos.PessoaDAO import PessoaDAO
from model.repositories.RepositorioPessoa import RepositorioPessoa
from colorama import Fore

conexao = Conexao.conectar_banco_dados()
cursor = conexao.cursor()
pessoaDAO = PessoaDAO(conexao)
repositorio = RepositorioPessoa(pessoaDAO)

if __name__ == '__main__':
    def exibir_menu():
        print("===============================")
        print(f"{Fore.LIGHTWHITE_EX}       SISTEMA DE PYTHON       {Fore.RESET}")
        print("===============================")
        print(f"1. {Fore.GREEN}Cadastrar{Fore.RESET}")
        print(f"2. {Fore.CYAN}Listar{Fore.RESET}")
        print(f"3. {Fore.YELLOW}Alterar{Fore.RESET}")
        print(f"4. {Fore.RED}Deletar{Fore.RESET}")
        print("5. Sair")
        print("===============================")

    def cadastrar():
        print("===============================")
        print(f"        {Fore.GREEN}TELA DE CADASTRO{Fore.RESET}        ")
        print("===============================\n")

        nome = str(input('Digite o nome da pessoa: '))
        email = str(input('Digite o email: '))
        telefone = str(input('Digite o telefone: '))
        idade = int(input('Digite a idade: '))
        
        cadastro = repositorio.adicionar_pessoa(nome, email, telefone, idade)
        return print(cadastro)

    def listar():
        pessoas = repositorio.listar_pessoas()
        for pessoa in pessoas:
            print(pessoa)

    def editar():
        print("===============================")
        print(f"        {Fore.YELLOW}TELA DE EDIÇÃO{Fore.RESET}         ")
        print("===============================\n")

        id_pesquisa = str(input('Digite o id da pessoa: '))
        id = repositorio.buscar_pessoa(id_pesquisa)

        if not id:
            print('Pessoa não encontrada.')
            return

        print(f'Pessoa encontrada!')
        
        nome = str(input('Digite o novo nome da pessoa: '))
        email = str(input('Digite o novo email: '))
        telefone = str(input('Digite o novo telefone: '))
        idade = int(input('Digite a nova idade: '))

        atualizado = repositorio.atualizar_pessoa(id_pesquisa, nome, email, telefone, idade)
        print(atualizado)

    def deletar():
        print("===============================")
        print(f"       {Fore.RED}TELA DE EXCLUSÃO{Fore.RESET}        ")
        print("===============================\n")

        id_pesquisa = str(input('Digite o id da pessoa: '))
        id = repositorio.buscar_pessoa(id_pesquisa)

        if not id:
            print('Pessoa não encontrada.')
            return

        print(f'Pessoa encontrada!')

        delete = repositorio.excluir_pessoa(id_pesquisa)
        print(delete)

    # Loop principal do programa
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break
        else:
            input("Opção inválida. Pressione Enter para continuar...")