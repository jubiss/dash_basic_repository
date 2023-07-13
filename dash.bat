@echo off

echo Venv Activation
call .env\Scripts\activate
echo Starting Dash server
python index.py
