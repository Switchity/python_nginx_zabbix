echo "# python_nginx_zabbix" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/Switchity/python_nginx_zabbix.git
git push -u origin master

## Create project directory
mkdir fastapi_project
cd fastapi_project

## Create virtual environment
python -m venv venv

## This often works even when python -m venv fails.
> virtualenv venv

## Activate it (Linux/Mac)
source venv/bin/activate

## Activate it (Windows)
venv\Scripts\activate

## Create directory structure
mkdir -p app/{models,schemas,routes,core} tests

## now install the required package 
>pip install -r requirements.txt

r: The -r flag tells pip to read the list of packages from the specified file.

## In case want to uninstall'
> pip uninstall -r requirements.txt -y

-y:  The -y flag automatically confirms the uninstallation for all packages

## create a requirements.txt file
> pip freeze > requirements.txt

🏗️ Architecture Overview
        ┌─────────────┐
Client →│   Nginx     │→ (Load Control, Rate Limit, Buffering)
        └─────┬───────┘
              │
       ┌──────▼─────────┐
       │ Python Service │  (FastAPI / Flask / Django REST)
       └──────┬─────────┘
              │
       ┌──────▼──────────┐
       │   Zabbix Agent  │ (On Python host & Nginx host)
       └──────┬──────────┘
              │
       ┌──────▼─────────┐
       │   Zabbix Server│ → Grafana / Zabbix UI
       └────────────────┘

Project Structure
python_nginx_zabbix/
├── api/                     # Python REST API (FastAPI)
│   ├── app.py
│   ├── requirements.txt
│   └── gunicorn_conf.py
├── nginx/
│   └── nginx.conf           # Reverse proxy + load control
├── zabbix/
│   ├── zabbix_agentd.conf   # Agent config
│   └── userparameters.conf  # Custom metrics
└── README.md                # Documentation


### run 
waitress-serve --listen=*:5000 app.app:app

or


### Run your application with Uvicorn:
uvicorn app.app:app --host 0.0.0.0 --port 8000


## now run nginx server as it take 8000 port
C:\Users\chandan\Downloads\nginx-1.28.0\nginx-1.28.0>.\nginx.exe -c "D:\python_nginx_zabbix\nginx\nginx.conf"

### if you will select the folder of nginx
> .\nginx.exe -c  "D:\python_nginx_zabbix\nginx\nginx.conf" '
## test
http://localhost:8080/