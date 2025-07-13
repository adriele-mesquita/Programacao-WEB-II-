@echo off
REM Script de build automático para Jenkins (Windows)
echo Iniciando processo de build do projeto Django Food Travel...

REM 1. Navegar para o diretório do projeto (
REM CD %WORKSPACE%

REM 2. Criar e Ativar o ambiente virtual
echo Verificando e criando ambiente virtual se necessario...
IF NOT EXIST venv\ (
    echo Criando ambiente virtual...
    python -m venv venv
    IF %ERRORLEVEL% NEQ 0 (
        echo ERRO: Falha ao criar o ambiente virtual.
        EXIT /B %ERRORLEVEL%
    )
)

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao ativar o ambiente virtual.
    EXIT /B %ERRORLEVEL%
)

REM 3. Instalar/Atualizar dependências Python
echo Instalando/Atualizando dependencias Python...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao instalar dependencias.
    EXIT /B %ERRORLEVEL%
)

REM 4. Aplicar migrações do banco de dados
echo Aplicando migracoes do banco de dados...
python manage.py migrate
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao aplicar migracoes.
    EXIT /B %ERRORLEVEL%
)

REM 5. Coletar arquivos estáticos (importante para deploy)
echo Coletando arquivos estaticos...
python manage.py collectstatic --noinput
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao coletar arquivos estaticos.
    EXIT /B %ERRORLEVEL%
)

REM 6. Rodar testes (se houver, adicione seus testes Django aqui)
echo Rodando testes Django...
python manage.py test
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Testes falharam.
    EXIT /B %ERRORLEVEL%
)

REM 7. Rodar a análise do SonarCloud
echo Rodando analise SonarCloud...
C:\Users\Adriele\Desktop\sonar-scanner-7.1.0.4889-windows-x64\bin\sonar-scanner.bat
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha na analise SonarCloud.
    EXIT /B %ERRORLEVEL%
)

echo Build do projeto Django Food Travel CONCLUIDO com sucesso!