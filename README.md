Установка зависимостей: 
```
python3 -m pip install uvicorn fastapi pymongo
```

Запуск MongoDB и сервера из директории src:
```
docker run -d -p 27017:27017 mongo
cd src
uvicorn main:app
```

По умолчанию, сервер запуститься на 127.0.0.1:8000. 

Документация: http://127.0.0.1:8000/docs

curl команды доступны в bash сценарии curl.sh