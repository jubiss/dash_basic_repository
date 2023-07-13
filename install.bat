@echo off

echo  Create Enviroment
python -m venv .env
call .env\Scripts\activate
echo Installing required Python packages...
python -m pip install -r requirements.txt
echo Installing component submodule
git submodule add https://github.com/jubiss/dash_custom_components.git
cd dash_custom_components
echo Installing requirements from coponents
pip install -r requirements.txt