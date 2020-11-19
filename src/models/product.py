from pydantic import BaseModel
from config.db import db
from bson.objectid import ObjectId

import re

product_collection = db['products']

class Product(BaseModel):
    """
    pydantic модель продукта. 
    """
    name: str
    description: str
    parametres: dict



def _find(filter: dict) -> list:
    """
    Отправляем запрос к базе данных и распаковывем его в виде списка.
    """
    res = []
    req=product_collection.find(filter)
    for record in req:
        print(1)
        res.append({
            'id': str(record['_id']),
            'name': record['name'],
            'description': record['description'],
            'parametres': record['parametres']
        })
    return res 

def add(product: Product) -> str:
    """
    Добавление записи в базу. Вернет id добавленного объекта.
    """
    res = product_collection.insert_one(product.dict())
    return str(res.inserted_id)

def get_by_id(id: str) -> list:
    """
    Поиск записи по id. Вернет список с 1 объектом, если запись будет найдена, в проитвном случае - вернет пустой список.
    """
    return _find({"_id": ObjectId(id)})

def get_by_name(name: str, is_full_match: bool = True) -> list:
    """
    Поиск записи по имени. 
        name - имя объекта; 
        is_full_match - указывает искать по польному совпадению (True), либо по вхождению элемента (False).
    """
    if is_full_match:
        return _find({"name": name})
    else:
        find_by_name = re.compile(name)
        return _find({"name": {"$regex": find_by_name}})


re_int = re.compile(r'^[0-9]+$')
re_float = re.compile(r'^[0-9]+\.[0-9]+$')
def get_by_parameter(parameter_key: str, parameter_value: str) -> list:
    """
    Поиск по параметру с указанным значением в базе данных.
        parameter_key - имя параметра;
        parameter_value - значение параметра.
    """
    if re_int.match(parameter_value) != None:
        parameter_value = int(parameter_value)
    elif re_float.match(parameter_value) != None:
        parameter_value = float(parameter_value)
    return _find({'parametres.{}'.format(parameter_key): parameter_value})