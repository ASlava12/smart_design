from fastapi import FastAPI


from models.product import Product


app = FastAPI()

@app.get('/')
def home():
    return "hello"
