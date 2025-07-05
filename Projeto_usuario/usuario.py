from dataclasses import dataclass
import string

@dataclass
class Usuario:
    """
    Classe que representa um usuário do sistema.
    Valida automaticamente nome, email e senha ao ser instanciado.

    """
    nome: str
    email: str
    senha: str

    def __post_init__(self):
        """
        Método chamado automaticamente após a criação da instância.
        Garante que os dados passados estejam corretos e seguros.

        """
        
        self.validar_nome(self.nome)
        self.validar_dominio(self.email)
        self.validar_senha(self.senha)
    
    def to_dict(self):
        """
        Converte os dados do usuário para um dicionário,
        facilitando a persistência em arquivos JSON.

        """
        return {
            'Nome': self.nome,
            'Email': self.email,
            'Senha': self.senha
        }
    
    @classmethod
    def from_dict(cls, dados):
        """
        Cria uma instância de Usuario a partir de um dicionário.
        Útil para carregar dados persistidos.

        :dados: dicionário contendo as chaves 'Nome', 'Email' e 'Senha'
        :return: instância da classe Usuario

        """
        return cls(
            nome=dados["Nome"],
            email=dados["Email"],
            senha=dados["Senha"]
        )

    @staticmethod
    def validar_nome(nome):
        caracteres = any(caracter in string.punctuation for caracter in nome)
        numeros_nao_permitido = any(char.isdigit() for char in nome)

        """
        Valida o nome do usuário.

        - Deve ser uma string
        - Não pode estar vazio
        - Mínimo 3 e máximo 50 caracteres
        - Sem números ou caracteres especiais
        - Deve ter nome e sobrenome


        """

        if not isinstance(nome, str):
            raise TypeError('O nome deve ser um caracter.')
        
        elif not (3 <= len(nome) <= 50):
            raise ValueError('O nome deve ter no minimo 3 e máximo 50 caracteres')
        
        elif caracteres:
            raise ValueError('Não é permitido ter caracteres especiais no nome')
        
        elif numeros_nao_permitido:
            raise ValueError('O nome não pode conter números.')
        
        elif not nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        
        elif len(nome.split()) < 2:
            raise ValueError('Coloque o nome e sobrenome no campo')
        
        else:
            print(f'Nome cadastrado: {nome}')

    @staticmethod
    def validar_dominio(email):

        """
        Valida o formato do e-mail.

        - Deve conter '@'
        - Deve conter 'gmail.com'
        - Não pode começar ou terminar com '@'
        - Não pode conter múltiplos '@' ou emails
        - O email deve terminar com @gmail.com, @hotmail.com ou @outlook.com.

        """

        lista_email = ['@gmail.com', '@hotmail.com',  '@outlook.com' ]
        email_correto = any(email.endswith(emails) for emails in lista_email)
        
        if not isinstance(email, str):
            raise TypeError('O e-mail deve ser uma caracter.')
        
        if not email.split():
            raise ValueError('E-mail não pode estar vazio.')
        
        elif (email[0] == '@') or (email[-1] == '@') or (email[0] == '.') or (email[-1] == '.'):
            raise ValueError('E-mail inválido: não pode começar ou terminar com "@" ou ".".')
        
        elif not email_correto:
            raise ValueError('O e-mail precisa terminar com @gmail.com, @hotmail.com ou @outlook.com.')
        
        elif (email.count('@') > 1) or (email.count('@gmail.com') > 1) or (email.count('@hotmail.com')> 1)  or (email.count('@outlook.com') > 1):
            raise ValueError('E-mails Não pode ser repetidos')
        
        else:
            print(f'E-mail registrado com sucesso: {email}')

    @staticmethod
    def validar_senha(senha):

        """
        Valida a força da senha.

        - Deve ter no mínimo 8 caracteres
        - A senha não pode passar de 64 caracteres
        - Deve conter letra maiúscula, minúscula, número
        - Deve conter ao menos um caracter especial
        - Não deve conter espaços vazios

        """

        minusculo = any(c.islower() for c in senha)
        maiusculo = any(c.isupper() for c in senha)
        numero = any(c.isdigit() for c in senha)

        checando_caracteres_especiais = any(c in string.punctuation for c in senha)

        if len(senha) < 8:
            raise ValueError('Senha fraca: mínimo 8 caracteres.')
        
        elif len(senha) > 64:
            raise ValueError('Senha muito longa: máximo 64 caracteres.')
        
        elif ' ' in senha:  
            raise ValueError('A senha não pode conter espaços')  
            
        elif (not minusculo) or (not maiusculo) or (not numero):
            raise ValueError('Senha fraca: deve conter letras minúsculas, maiúsculas e números.')
        
        elif not checando_caracteres_especiais:
            raise ValueError('Senha fraca: inclua pelo menos um caractere especial.')
        
        else:
            print('Senha criada com sucesso')

