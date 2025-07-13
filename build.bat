@echo off
REM 
echo Iniciando processo de build do projeto Django Food Travel...

REM 
REM 

REM
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao ativar o ambiente virtual.
    EXIT /B %ERRORLEVEL%
)

REM 
echo Instalando/Atualizando dependencias Python...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao instalar dependencias.
    EXIT /B %ERRORLEVEL%
)

REM 
echo Aplicando migracoes do banco de dados...
python manage.py migrate
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao aplicar migracoes.
    EXIT /B %ERRORLEVEL%
)

REM 
echo Coletando arquivos estaticos...
python manage.py collectstatic --noinput
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao coletar arquivos estaticos.
    EXIT /B %ERRORLEVEL%
)

REM 
echo Rodando testes Django...
python manage.py test
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Testes falharam.
    EXIT /B %ERRORLEVEL%
)

echo Build do projeto Django Food Travel CONCLUIDO com sucesso!