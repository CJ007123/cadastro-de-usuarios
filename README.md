# 🔐 Sistema de Gerenciamento de Usuários em Python

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da Programação Orientada a Objetos (POO) em Python, incluindo:

- Criação de classes e objetos
- Validação de dados do usuário
- Encapsulamento de lógica de negócio
- Controle de login e autenticação
- Manipulação de arquivos JSON para persistência de dados

---

## 📌 Funcionalidades

✅ Criar conta com nome, e-mail e senha  
✅ Validação de nome, e-mail e senha com regras claras  
✅ Login e logout  
✅ Exibir dados da conta logada  
✅ Alterar nome, e-mail ou senha (com validação)  
✅ Remover conta  
✅ Salvamento e carregamento de contas com JSON  
✅ Menu interativo com tratamento de erros  

---

## 🛠️ Tecnologias utilizadas

- [Python 3.12.1]
- Módulos nativos: `dataclasses`, `json`, `string`

---

## 📂 Estrutura das Classes

### `Usuario`
Classe que representa o usuário com os seguintes atributos:
- `nome` (str)
- `email` (str)
- `senha` (str)

Cada dado é validado automaticamente no momento da criação do objeto com o método especial `__post_init__`.

Também possui:
- `to_dict()` → transforma o objeto em dicionário (para salvar)
- `from_dict()` → recria o objeto a partir de um dicionário (para carregar)

### `GerenciamentoDeUsuario`
Classe responsável por:
- Adicionar usuários (com verificação de duplicidade)
- Realizar login/logout
- Alterar informações da conta logada
- Exibir ou remover conta
- Salvar ou carregar usuários via arquivo JSON

---

## 🎯 Regras de Validação

### Nome:
- Deve ser uma string
- Não pode ser vazio

### E-mail:
- Deve conter `@` e `gmail.com`
- Não pode conter mais de um `@` ou `gmail.com`
- Não pode começar ou terminar com `@`

### Senha:
- Mínimo de 8 caracteres
- Pelo menos 1 letra minúscula
- Pelo menos 1 letra maiúscula
- Pelo menos 1 número
- Pelo menos 1 caractere especial (ex: `@`, `#`, `!`)

---

## 💡 Como usar?

1. Clone este repositório:
```bash
git clone https://github.com/CJ007123/cadastro-de-usuarios.git

