@echo off

echo  Create Enviroment
python -m venv .env
call .env\Scripts\activate
echo Installing required Python packages...
python -m pip install -r requirements.txt