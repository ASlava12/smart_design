Установка зависимостей: 
```
python3 -m pip install uvicorn fastapi pymongo
```

Запуск сервера из директории src:
```
cd src
uvicorn main:app
```

По умолчанию, сервер запуститься на 127.0.0.1:8000. 

Документация: http://127.0.0.1:8000/docs

curl команды доступны в bash сценарии curl.sh