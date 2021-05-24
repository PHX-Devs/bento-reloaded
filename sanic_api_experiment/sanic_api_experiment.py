from sanic import Sanic
from sanic.response import text, json
from sanic_openapi import swagger_blueprint

app = Sanic("sanic_api_experiment")
app.config.FORWARDED_SECRET = "sanic_api_experiment"
app.blueprint(swagger_blueprint)

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4043, workers=8, access_log=False)
