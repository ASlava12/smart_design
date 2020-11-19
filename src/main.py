from fastapi import FastAPI
from typing import Optional


import models.product as product


app = FastAPI()

@app.get('/')
def home():
    return "hello"

@app.post('/addProduct')
def addProduct(item: product.Product):
    return {
        "result": product.add(item)
    }

@app.get('/getProductByName/{name}')
def getProductByName(name: str, is_full_match: Optional[bool] = True):
    return {
        'result': product.get_by_name(name, is_full_match)
    }

@app.get('/getProductByID/{id}')
def getProductByID(id: str):
    return {
        'result': product.get_by_id(id)
    }

@app.get('/getProductByParameter/{parameter_name}/{parameter_value}')
def getProductByParameter(parameter_name: str, parameter_value):
    return {
        'result': product.get_by_parameter(parameter_name, parameter_value)
    }