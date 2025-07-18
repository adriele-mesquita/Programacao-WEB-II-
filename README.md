
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

5.  Crie usuários iniciais:
    Para testar o login e o CRUD, você pode criar um cliente e um python manage.py shell
    No shell Python, execute:
    from django.contrib.auth.models import User
    from core.models import Cliente, Funcionario, Restaurante

    Criar um Restaurante (necessário para criar Funcionario e alguns Produtos/Pedidos)
    restaurante, created = Restaurante.objects.get_or_create(
        nome_do_restaurante='Restaurante Central',
        defaults={
            'cnpj': '00000000000000',
            'endereco_restaurante': 'Av. Principal, 100',
            'horario_funcionamento': '09:00:00'
        }
    )
    if created:
        print(f"Restaurante '{restaurante.nome_do_restaurante}' criado.")
    else:
        print(f"Restaurante '{restaurante.nome_do_restaurante}' já existe.")

    user_cliente, created = User.objects.get_or_create(username='cliente_teste', defaults={'email': 'cliente@exemplo.com'})
    if created:
        user_cliente.set_password('senhadocliente')
        user_cliente.save()
        Cliente.objects.create(user=user_cliente, nome='Cliente Teste', cpf='11111111111', telefone='11999998888', email='cliente@exemplo.com')
        print(f"Cliente '{user_cliente.username}' criado.")
    else:
        print(f"Usuário cliente '{user_cliente.username}' já existe.")

    user_funcionario, created = User.objects.get_or_create(username='funcionario_master', defaults={'email': 'funcionario@exemplo.com'})
    if created:
        user_funcionario.set_password('senhadofuncionario')
        user_funcionario.is_staff = True
        user_funcionario.is_superuser = True
        user_funcionario.save()
        Funcionario.objects.create(user=user_funcionario, nome_funcionario='Funcionario Master', cargo='Gerente', data_contratacao='2023-01-01', salario=5000.00, id_restaurante=restaurante)
        print(f"Funcionário Master '{user_funcionario.username}' criado.")
    else:
        print(f"Usuário funcionário '{user_funcionario.username}' já existe.")

    exit()
    ```
    
6. Inicie o servidor de desenvolvimento:
    python manage.py runserver

7.  Abra seu navegador e acesse `http://127.0.0.1:8000/`.

Painel de Administração:`http://127.0.0.1:8000/admin/`
Lista de Produtos (CRUD):`http://127.0.0.1:8000/produtos/`