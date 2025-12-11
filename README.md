# Beginning of Elden - RPG Character Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Um sistema robusto de gerenciamento de personagens de RPG via linha de comando (CLI), desenvolvido em **Python** com persistência de dados em **MySQL**. O projeto foca em lógica de jogo orientada a objetos, herança de classes e manipulação de inventários inspirados no universo de *Elden Ring*.

---

## 📸 Funcionalidades e Demonstração

### 1. Sistema de Autenticação e Menu Principal
O sistema conta com um fluxo seguro de **Login e Registro**. As senhas dos usuários nunca são salvas em texto puro; utilizamos **hashing** para garantir a segurança dos dados antes da inserção no banco.

![Menu Principal e Login](https://github.com/user-attachments/assets/ca164e75-d0e3-43b7-b78d-ce8771058edb)

### 2. Criação de Personagem Interativa
Interface via terminal robusta que valida as entradas do usuário (como idade e strings vazias). O sistema instancia classes específicas (Herança) baseadas na escolha do jogador (Ex: `Vagabundo`, `Samurai`, `Miserável`).

![Criação de Personagem](https://github.com/user-attachments/assets/a87c3571-0bca-4e73-a0ed-e5ce2cee9e11)

### 3. Sistema de Builds Automatizadas
Um dos diferenciais do projeto. Após escolher a classe, o usuário seleciona uma "Build" específica. O código Python aplica automaticamente modificadores de atributos e adiciona itens ao inventário do objeto, demonstrando lógica de jogo complexa.

![Sistema de Builds](https://github.com/user-attachments/assets/89ad1001-2d36-4846-abab-4da522ca3869)

### 4. Persistência e Recuperação de Dados
Exemplo de uma ficha completa recuperada do banco de dados MySQL. O sistema realiza o *parsing* de listas salvas como JSON para exibir o inventário (Equipamentos e Roupas) de forma legível para o usuário.

![Ficha do Personagem](https://github.com/user-attachments/assets/67df1bff-11e2-4529-bbba-d3c32a0e36c7)

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* **Python 3.8+**
* **Servidor MySQL** (Local ou Remoto)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/dvx0exe/beginning-of-elden.git](https://github.com/dvx0exe/beginning-of-elden.git)
    cd beginning-of-elden
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuração do Banco de Dados:**
    * Crie um banco de dados no seu MySQL.
    * Execute o script `per.sql` incluído no projeto para criar as tabelas necessárias.

4.  **Variáveis de Ambiente:**
    * Renomeie o arquivo `.env.example` para `.env`.
    * Configure as credenciais do seu banco de dados:
    ```ini
    DB_HOST=localhost
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_NAME=nome_do_banco
    ```

5.  **Executar:**
    ```bash
    python app.py
    ```

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Banco de Dados:** MySQL
* **Bibliotecas Principais:**
    * `mysql-connector-python`: Conexão com o banco.
    * `python-dotenv`: Gerenciamento de variáveis de ambiente.
    * `hashlib` (Nativa): Segurança de senhas.
    * `json` (Nativa): Manipulação de estrutura de dados complexos.

---
*Este projeto foi desenvolvido para fins educacionais, demonstrando competências em Back-end, POO e Banco de Dados.*
