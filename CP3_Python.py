import os

# Dados do Usuario E Do Filme.
consulta_Filmes = [{'nome': "Palmeiras", 'genero': "Campeão Mundial", 'ano': '1951', 'sinopse': 'FIFA Reconhece Palmeiras Como PRIMEIRO Campeão Mundial de 1951. Vencendo a Juventus.'}]
verifica_cadastro = {}

# Funçõo Para Mostar a LogoMarca
def logomarca():
    print("★  ℕ𝕖𝕥𝕗𝕝𝕚𝕩 𝕕𝕖 ℂ𝕙𝕖𝕣𝕟𝕠𝕓𝕪𝕝  ★")
# Funçõo Para Mostrar o MENU Inicial
def menu_cadastro():
    print("Digite (1) - Cadastro.")
    print("Digite (2) - Login.")
    print("Digite (3) - Cadastro De Filmes.")
    print("Digite (4) - Remover Usuario.")
    print("Digite (5) - Sair.")
# Funçõo Para Voltar ao MENU
def voltar_ao_menu_principal():
    input("\nDigite uma tecla para retornar ao menu: ")
    #os.system('cls') 
    #os.system('clear')
# Funçõo Para Consultar e Assistir os filmes
def consulta():
    print("Opção Escolhida (4) - Consultar Filmes Cadastrados.")
    print(f"""{'Nome Do Filme'.ljust(21)} | {'Gênero'.ljust(22)} | {'Ano'.ljust(20)} | """)
    for i, dado in enumerate(consulta_Filmes, 1):
        nome_do_filme = dado['nome']
        genero_do_filme = dado['genero']
        ano_do_filme = dado['ano']
        sinopse_do_filme = dado['sinopse']
        print(f'{i}- {nome_do_filme.ljust(20)} | {genero_do_filme.ljust(22)} | {ano_do_filme.ljust(20)} | ')
        
    assistir = int(input("\n|Digite o Numero do Filme que deseja Assistir |\n|Digite o Numero 0 Para Voltar Ao Menu De Filmes.|"))

    if assistir == 0:
        print("Voltando Ao Menu De Filmes.")
        menu_filme()
    elif 1 <= assistir <= len(consulta_Filmes):
        filme_escolhido = consulta_Filmes[assistir - 1]
        print(f"Você escolheu assistir '{filme_escolhido['nome']}'")
        print(f"Sinopse: {filme_escolhido['sinopse']}")
        print("Bom Filme!")
        print("Envie Uma Mensagem Quando Terminar O Filme.")
        voltar_ao_menu_principal()
    else:
        print("Opção Inválida. Por favor, escolha um número válido.")
        consulta()     
# Funçõo Para ecolher uma opção do MENU CADASTRO
def escolha_opcao():
    opcao = int(input("Digite o Numero Conforme Seu Desejo: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        login()
    elif opcao == 3:
        necessario_login()
    elif opcao == 4:
        print("Digite o Numero Do Usuario que Deseja Remover.")
        remove_usuario()
    elif opcao == 5:
        print("Saindo Da Netflix.")
    else:
        print("Opção inválida. Tente novamente.")
        menu_cadastro()
        escolha_opcao()
# Funçõo  Para Remover Um Usuario
def remove_usuario():
    if verifica_cadastro:
        for i, (email, usuario) in enumerate(verifica_cadastro.items(), 1):
            print(f"{i}. {usuario['nome']} (Email: {email})")
        remover_usuario = int(input("Escolha o número do Usuário que deseja remover: "))
        if 1 <= remover_usuario <= len(verifica_cadastro):
            email_para_remover = list(verifica_cadastro.keys())[remover_usuario - 1]
            del verifica_cadastro[email_para_remover]
            print("Usuário removido com sucesso!")
        else:
            print("Número inválido! Por favor, escolha um número válido.")
    else:
        print("Não há usuários cadastrados.")
    menu_cadastro()
    escolha_opcao()
# Funçõo Para Cadastro Pessaal
def cadastro():
    while True:
        print("Opção Escolhida (1) - Cadastro.")
        nome = input("Digite seu nome: ")
        idade = input("Digite sua Idade: ")
        cel = input("Digite seu Telefone: ")
        email = input("Digite seu E-mail: ")
        senha = input("Digite sua senha: ")
        confirma_senha = input("Confirme sua senha: ")

        if not nome or not email or not senha:
            print("Nome, E-mail e Senha não podem ser vazios.")
            continue

        if senha != confirma_senha:
            print("Senhas não coincidem. Tente novamente.")
            continue

        verifica_cadastro[email] = {'nome': nome, 'email': email, 'senha': senha, 'idade': idade, 'telefone': cel}
        print(f"Seus Dados estão corretos?\nNome: {nome}\nIdade: {idade}\nTelefone: {cel}\nE-mail: {email}\nSenha: {senha}")
        dados()
        break
# Funçõo Para Verificar se os Dados Estão Corretos.
def dados():
    resposta_usuario = int(input("Digite (1)- Para Dados Corretos.\nDigite (2) - Para dados Incorretos.\n"))
    if resposta_usuario == 1:
        print("Cadastrado com Sucesso!")
        voltar_ao_menu_principal()
        menu_filme()
        escolha_opcao()
    elif resposta_usuario == 2:
        print("Refazendo Cadastro.")
        cadastro()
    else:
        print("Opção Inválida. Tente Novamente.")
        dados()
# Funçõo Para Fazer lOGIN
def login():
    print("Opção Escolhida (2) - Login.")
    email = input("Digite seu email: ")

    if email in verifica_cadastro:
        senha = input("Digite sua senha: ")
        if senha == verifica_cadastro[email]['senha']:
            print("Logado Com Sucesso!")
            cadastro_filmes()
        else:
            print("Senha Incorreta. Tente Novamente.")
            login()
    else:
        print("Email não encontrado. Tente novamente.")
        engano = int(input("Se Você Selecionou essa Opção Por Engano, Digite (1) Para Voltar Ao Menu Principal.\nCaso Queira Tentar Novamente o Email, Digite (2): "))
        if engano == 1:
            menu_cadastro()
            escolha_opcao()
        elif engano == 2:
            login()
        else:
            print("Opção Inválida. Tente Novamente.")
            login()
# Funçõo Para ver o MENU DE FILMES E ESCOLHE OPÇÃO DO FILME
def menu_filme():
    logomarca()
    print("Digite (1) Para Consultar Filmes Cadastrados.")
    print("Digite (2) Para Remover Um Filme.")
    print("Digite (3) Para Cadastrar Novo Filme.")
    print("Digite (4) Para Voltar ao Menu Principal.")

    opcao_filme = int(input("Escolha uma opção: "))
    if opcao_filme == 1:
        consulta()
        voltar_ao_menu_principal()
        menu_filme()
    elif opcao_filme == 2:
        print("===== FILMES CADASTRADOS =====")
        for i, filme in enumerate(consulta_Filmes, 1):
            print(f"{i}. {filme['nome']}")
        filme_remover = int(input("Escolha o número do filme que deseja remover: "))
        if 1 <= filme_remover <= len(consulta_Filmes):
            del consulta_Filmes[filme_remover - 1]
            print("Filme removido com sucesso!")
        else:
            print("Número inválido! Por favor, escolha um número válido.")
        menu_filme()
    elif opcao_filme == 3:
        cadastro_filmes()
    elif opcao_filme == 4:
        voltar_ao_menu_principal()
        menu_cadastro()
        escolha_opcao()
    else:
        print("Opção Inválida!")
        menu_filme()
# Funçõo Para Cadastrar Filmes
def cadastro_filmes():
    logomarca()
    print("- Cadastro de Filmes.")
    nome_filme = input("Nome do Filme: ")
    genero_filme = input("Gênero do Filme: ")
    ano_filme = input("Ano do Filme: ")
    sinopse_filme = input("Sinopse do Filme: ")
    print("Filme Cadastrado com Sucesso!")
    print(f"Os dados do filme estão corretos?\nNOME: {nome_filme}\nGÊNERO: {genero_filme}\nANO: {ano_filme}\nSINOPSE: {sinopse_filme}\n")
    resposta_usuario = int(input("Digite (1)- Para Dados Corretos.\nDigite (2) - Para dados Incorretos.\n"))
    if resposta_usuario == 1:
        cadastrar_Filmes = {'nome': nome_filme, 'genero': genero_filme, 'ano': ano_filme, 'sinopse': sinopse_filme}
        consulta_Filmes.append(cadastrar_Filmes)
        print("Filme Cadastrado com Sucesso!")
        voltar_ao_menu_principal()
        menu_filme()
    elif resposta_usuario == 2:
        print("Redirecionando Para Cadastro De Filmes.")
        cadastro_filmes()
    else:
        print("Opção Inválida. Tente Novamente.")
        cadastro_filmes()
# Funçõo Para Caso O Usuario Tente Ir Direto Para O Cadastro De Filmes
def necessario_login():
    print("Para fazer o Cadastro De Filmes é Necessário Fazer Login.")
    pergunta = input("Você Possui Cadastro? (S/N): ").upper()
    if pergunta == "S":
        login()
    elif pergunta == "N":
        cadastro()
    else:
        print("Opção Inválida. Digite (S - Para Sim | N - Para Não)")
        necessario_login()
# Funçõo Main
def main():
    logomarca()
    menu_cadastro()
    escolha_opcao()

if __name__ == "__main__":
    main()

    main()