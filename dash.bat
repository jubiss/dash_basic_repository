@echo off

echo ativacao do venv juliana_comercial
call .env\Scripts\activate
echo Rodando servidor de dash 
python index.py
