
Este é o projeto da disciplina de Programação WEB II, desenvolvido como uma aplicação webII utilizando o Django.

Discente: Adriele Mesquita
Disciplina:Programação WEB II
Utilizamos:
 Python
 Django
 HTML5
 CSS3
 SQLite 3
 Git / GitHub
 Katalon para testes automatizados 
 Jenkins para build automática
 SonarCloud para análise de código

O objetivo deste projeto é desenvolver uma aplicação de delivery de comida, "Food Travel", que permita aos usuários explorar um cardápio variado, fazer pedidos e interagir com o sistema. O projeto tem:
 Entidades e Modelos de Banco de Dados (10 entidades)
 Operações CRUD (Criar, Ler, Atualizar, Deletar)
 Injeção de Dependência
 Controle de Versão com Git/GitHub
 Automação de Build com Jenkins
 Testes Automatizados com Katalon
 Análise de Qualidade de Código com SonarCloud

 Como Rodar o Projeto Localmente
1.  Clone o repositório:
    git clone (https://github.com/adriele-mesquita/Programacao-WEB-II-.git)
    cd Programacao-WEB-II
    
2.  Crie e ative o ambiente virtual:
    python -m venv venv
     Windows
    .\venv\Scripts\activate
     macOS/Linux
    source venv/bin/activate
    
3.  Instale as dependências:
    pip install Django

4.  Aplique as migrações do banco de dados:
    python manage.py makemigrations core
    python manage.py migrate

5.  Crie um superusuário:
    python manage.py createsuperuser
    Siga as instruções para criar o nome de usuário e senha.
    
6. Inicie o servidor de desenvolvimento:
    python manage.py runserver

7.  Abra seu navegador e acesse `http://127.0.0.1:8000/`.

Painel de Administração:`http://127.0.0.1:8000/admin/`
Lista de Produtos (CRUD):`http://127.0.0.1:8000/produtos/`