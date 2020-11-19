from pydantic import BaseModel
from config.db import db
from bson.objectid import ObjectId

import re

product_collection = db['product']

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
    for record in product_collection.find(filter):
        res.append(record)
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

def get_by_parameter(parameter_key: str, parameter_value: str) -> list:
    """
    Поиск по параметру в базе данных.
        parameter_key - имя параметра;
        parameter_value - значение параметра.
    """
    return _find({'parametres.{}'.format(parameter_key): parameter_value})