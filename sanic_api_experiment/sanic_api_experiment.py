import sys
from sanic import Sanic
from sanic.response import text, json
from sanic_openapi import doc, swagger_blueprint
sys.path.append('..')
from utils.db import simple_query, delete_row, insert_row, update_row

app = Sanic("sanic_api_experiment")
app.config.FORWARDED_SECRET = "sanic_api_experiment"
app.blueprint(swagger_blueprint)

# https api scheme
app.config["API_SCHEMES"] = ["https"]
# Description
app.config["API_DESCRIPTION"] = "An example Swagger from Sanic-OpenAPI"

class NewEntree():
    entree_name = doc.String("The name of your entree.")

class Entree():
    entree_id = doc.Integer("Entree id.")

@app.get("/")
async def root(request):
    return json({"Hello": "World"})

@app.post("/entrees")
async def create_entree(request):
    """
    Create an entree
    - **entree_name**: each entree must have a name
    """
    entree_id = insert_row("INSERT INTO test.entree (entree_name) VALUES (:entree_name) RETURNING entree_id", entree.dict())

    return json({"created": True, "entree_id": entree_id, "entree_name": entree.entree_name})

    return Entree(entree_id=entree_id, entree_name=entree.entree_name)


@app.get("/test")
@doc.consumes(doc.String(name="name"), location="query")

@app.post("/test")
@doc.consumes(
    doc.JsonBody(
        {
            "useranme": doc.String("The name of your user account."),
            "password": doc.String("The password of your user account."),
        }
    ),
    location="body",
)
async def test(request):
    return json({})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4043, workers=8, access_log=False)
