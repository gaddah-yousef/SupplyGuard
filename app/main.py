from fastapi import FastAPI

app= FastAPI(title="SupplyGuard Demo API",description="Petite API utilisée pour tester la chaîne DevSecOps SupplyGuard.",version="0.1.0")

@app.get( "/health")
def health_check():
    return{"status":"ok"}
@app.get("/products")
def list_products():
    return [
        {"id":1 ,"name":"Clavier"
    },
    {
        "id":2 , "name":"Souris"
    }
    ]
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"id": product_id, "name": "Produit de démonstration"}
