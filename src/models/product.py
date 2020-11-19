from pydantic import BaseModel
from config import db
from pymongo import MongoClient


product_collection = MongoClient(db.host,db.port)[db.name]['product']

class Product(BaseModel):


    name: str
    description: str
    parametres: dict

def add(product : Product):
    pass

def get_by_id(id : str) -> Product:
    pass

def get_by_name(name : str) -> Product:
    pass

def get_by_parameter(parameter : str) -> Product:
    pass


