from dataclasses import dataclass, field
from usuario import Usuario
import json


@dataclass 
class GerenciamentoDeUsuario:
    """
    Classe responsável por gerenciar operações com usuários:
    - Cadastro
    - Login
    - Atualizações
    - Remoção
    - Persistência em arquivo JSON
    
    """
    usuario: list = field(default_factory=list)
    conta_login = None  # Representa o usuário atualmente logado

    def adicionar_usuario(self, conta: Usuario):
        """
        Adiciona um novo usuário à lista de contas registradas.
        Garante que não haja duplicatas com base no e-mail.

        :conta: Instância da classe Usuario

        """
        if not isinstance(conta, Usuario):
            raise ValueError('Conta inválida. Insira um objeto da classe Usuario.')

        for item in self.usuario:
            if getattr(item, 'email') == conta.email:
                raise ValueError('Este e-mail já está em uso.')

        self.usuario.append(conta)
        print(f'Sua conta foi adicionada com sucesso {conta.nome}!')

    def login(self, email:str, senha: str):
        """
        Realiza o login do usuário com base no e-mail e senha.
        Armazena a conta logada no atributo `conta_login`.

        :email: e-mail de login
        :senha: senha de login

        """
        if not self.usuario:
            raise ValueError('Nenhuma conta cadastrada.')

        for conta in self.usuario:
            if email == conta.email and senha == conta.senha:
                self.conta_login = conta
                print('Login feito com sucesso')
                return
        raise ValueError('E-mail ou senha estão incorretos')

    def logout(self):
        """
        Realiza o logout da conta logada, removendo a referência interna.

        """
        self.conta_login = None

    def exibir_conta(self):
        """
        Exibe os dados da conta logada. 
        Apenas possível se houver login ativo.

        """
        if not self.conta_login:
            raise PermissionError('Você precisa estar logado para visualizar os dados.')
        else:
            print(f'Nome: {self.conta_login.nome}\nEmail: {self.conta_login.email}\nSenha: {self.conta_login.senha}')

    def alterar_nome(self, novo_usuario: str):
        """
        Atualiza o nome da conta logada, validando a entrada.

        :novo_usuario: Novo nome do usuário

        """

        if not self.conta_login:
            raise PermissionError('Login necessário para realizar alterações.')
        else:
            Usuario.validar_nome(novo_usuario)
            self.conta_login.nome = novo_usuario
            print(f'Nome atualizado para: {novo_usuario}')

    def alterar_email(self, novo_email:str):
        """
        Atualiza o e-mail da conta logada, com validação.

        :novo_dominio: Novo domínio

        """
        if not self.conta_login:
            raise PermissionError('Login necessário para realizar alterações.')
        else:
            Usuario.validar_dominio(novo_email)
            self.conta_login.email = novo_email
            print(f'E-mail atualizado para: {novo_email}')

    def alterar_senha(self, nova_senha: str):
        """
        Atualiza a senha da conta logada, com verificação de segurança.

        :nova_senha: Nova senha

        """
        if not self.conta_login:
            raise PermissionError('Login necessário para realizar alterações.')
        else:
            Usuario.validar_senha(nova_senha)
            self.conta_login.senha = nova_senha
            print(f'Senha atualizada com sucesso.')

    def remover_conta(self, conta: Usuario):
        """
        Remove uma conta do sistema. Se for a conta logada, o login também é desfeito.

        :conta: instância da classe Usuario a ser removida

        """
        if not self.usuario:
            raise ValueError('Não há contas cadastradas para remover.')
        else:
            self.usuario.remove(conta)
            print(f'Conta {conta.email} foi removida!')
            self.conta_login = None

    def salvar_conta(self, caminho='usuario.json'):
        """
        Salva todas as contas registradas no sistema em um arquivo JSON.

        :caminho: Nome do arquivo onde os dados serão armazenados

        """
        dados = [usuario.to_dict() for usuario in self.usuario]
        with open(caminho, 'w', encoding='utf-8') as arquivos:
            json.dump(dados, arquivos, indent=4, ensure_ascii=False)
            print('Os dados foram salvos no sistema.')
            

    def carregar_conta(self, caminho='usuario.json'):
        """
        Carrega os dados de usuários salvos no JSON para a aplicação.

        :caminho: Caminho do arquivo JSON contendo os dados

        """
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivos:
                dados = json.load(arquivos)
                self.usuario = [Usuario.from_dict(d) for d in dados]
                print(f'Dados carregados com sucesso: {dados}')
        except FileNotFoundError:
            self.usuario = []
            print('Nenhum arquivo encontrado. Iniciando sistema vazio.')




