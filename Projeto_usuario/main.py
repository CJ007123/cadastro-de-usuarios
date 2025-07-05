from gerenciamento_de_usuario import GerenciamentoDeUsuario
from usuario import Usuario

menu = '''
🔐 MENU DO SISTEMA DE USUÁRIO 🔐
[1] Criar nova conta
[2] Fazer login
[3] Exibir conta
[4] Alterar nome
[5] Alterar e-mail
[6] Alterar senha
[7] Remover conta
[8] Logout
[9] Sair do sistema (salvar dados)
[10] Carregar dados manualmente

'''


def main(): 
    usg = GerenciamentoDeUsuario()
    # usg.carregar_conta()

    while True:
        try:
            opcao = int(input(menu))

            if opcao == 1:
                print('\n📝 Cadastro de novo usuário:')
                nome = input('Digite seu nome: ')
                email = input('Digite seu e-mail: ')
                senha = input('Crie uma senha segura: ')
                us1 = Usuario(nome, email, senha)
                usg.adicionar_usuario(us1)
                
            elif opcao == 2:
                print('\n🔐 Login na conta:')
                email = input('E-mail: ')
                senha = input('Senha: ')
                usg.login(email, senha)

            elif opcao == 3:
                if not usg.conta_login:
                    print('⚠️ Você precisa estar logado para exibir sua conta.')
                    continue
                usg.exibir_conta()
            
            elif opcao == 4:
                if not usg.conta_login:
                    print('⚠️ Faça login antes de tentar alterar o nome.')
                    continue
                novo_nome = input('Digite o novo nome: ')
                usg.alterar_nome(novo_nome)

            elif opcao == 5:
                if not usg.conta_login:
                    print('⚠️ Faça login antes de tentar alterar o e-mail.')
                    continue
                novo_email = input('Digite o novo e-mail: ')
                usg.alterar_email(novo_email)
                
            elif opcao == 6:
                if not usg.conta_login:
                    print('⚠️ Faça login antes de tentar alterar a senha.')
                    continue
                nova_senha = input('Digite a nova senha: ')
                usg.alterar_senha(nova_senha)

            elif opcao == 7:
                if not usg.conta_login:
                    print('⚠️ Faça login antes de tentar remover a conta.')
                    continue
                usg.remover_conta(usg.conta_login)

            elif opcao == 8:
                usg.logout()
                print('👋 Logout realizado com sucesso.')

            elif opcao == 9:
                usg.salvar_conta()
                print('💾 Dados salvos com sucesso. Saindo do sistema...')
                break

            elif opcao == 10:
                usg.carregar_conta()
                print('📂 Dados carregados com sucesso!')
            
            else:
                print('❌ Opção inválida. Tente novamente.')


        except ValueError as v:
            print(f'Erro: {v}')



if __name__ == '__main__':
    main()
