beginning-of-elden
Gerenciador de Personagens RPG - Python &amp; MySQL

1. Sistema de Autenticação e Menu Principal
O sistema conta com um fluxo seguro de **Login e Registro**. As senhas dos usuários nunca são salvas em texto puro; utilizamos **hashing** para garantir a segurança dos dados antes da inserção no banco.

<img width="299" height="473" alt="Captura de tela 2025-11-26 211601" src="https://github.com/user-attachments/assets/ca164e75-d0e3-43b7-b78d-ce8771058edb" />


2. Criação de Personagem Interativa
Interface via terminal robusta que valida as entradas do usuário (como idade e strings vazias). O sistema instancia classes específicas (Herança) baseadas na escolha do jogador (Ex: `Vagabundo`, `Samurai`, `Miserável`).

<img width="1011" height="617" alt="Captura de tela 2025-11-26 211756" src="https://github.com/user-attachments/assets/a87c3571-0bca-4e73-a0ed-e5ce2cee9e11" />


4. Sistema de Builds Automatizadas
Um dos diferenciais do projeto. Após escolher a classe, o usuário seleciona uma "Build" específica. O código Python aplica automaticamente modificadores de atributos e adiciona itens ao inventário do objeto, demonstrando lógica de jogo complexa.

<img width="1135" height="748" alt="Captura de tela 2025-11-26 211813" src="https://github.com/user-attachments/assets/89ad1001-2d36-4846-abab-4da522ca3869" />


4. Persistência e Recuperação de Dados
Exemplo de uma ficha completa recuperada do banco de dados MySQL. O sistema realiza o *parsing* de listas salvas como JSON para exibir o inventário (Equipamentos e Roupas) de forma legível para o usuário.

<img width="497" height="718" alt="Captura de tela 2025-11-26 212034" src="https://github.com/user-attachments/assets/67df1bff-11e2-4529-bbba-d3c32a0e36c7" />
