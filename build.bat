@echo off
REM Script de build automático
echo Iniciando processo de build do projeto Django Food Travel...

REM 1. Navegar para o diretório do projeto 
REM CD %WORKSPACE%
echo Diretorio de trabalho atual: %CD%

REM **NOVO**: Verificar se o Python esta no PATH do Jenkins
echo Verificando onde o python esta...
where python
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: O executavel 'python' nao foi encontrado no PATH do Jenkins. Certifique-se que o Python esta instalado no servidor e no PATH do Jenkins.
    EXIT /B %ERRORLEVEL%
)
echo Python encontrado no PATH do Jenkins.

REM 2. Criar e Ativar o ambiente virtual
echo Verificando e criando ambiente virtual se necessario...
IF NOT EXIST venv\ (
    echo Criando ambiente virtual com 'python -m venv venv'...
    python -m venv venv
    IF %ERRORLEVEL% NEQ 0 (
        echo ERRO: Falha ao criar o ambiente virtual com 'python -m venv venv'. Codigo de erro: %ERRORLEVEL%
        EXIT /B %ERRORLEVEL%
    )
    echo Ambiente virtual criado com sucesso.
) ELSE (
    echo Ambiente virtual 'venv' ja existe.
)

REM **NOVO**: 
echo Verificando conteudo da pasta venv\Scripts...
dir venv\Scripts\
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: A pasta 'venv\Scripts\' nao foi encontrada apos a tentativa de criacao do ambiente virtual.
    EXIT /B %ERRORLEVEL%
)
echo Conteudo da pasta venv\Scripts\ listado.

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao ativar o ambiente virtual com 'call venv\Scripts\activate.bat'. Codigo de erro: %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)
echo Ambiente virtual ativado.

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

REM 5. Coletar arquivos estáticos 
echo Coletando arquivos estaticos...
python manage.py collectstatic --noinput
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Falha ao coletar arquivos estaticos.
    EXIT /B %ERRORLEVEL%
)

REM 6. Rodar testes 
echo Rodando testes Django...
python manage.py test
IF %ERRORLEVEL% NEQ 0 (
    echo ERRO: Testes falharam.
    EXIT /B %ERRORLEVEL%
)



echo Build do projeto Django Food Travel CONCLUIDO com sucesso!