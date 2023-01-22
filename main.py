from api import API

app = API()


@app.route("/home")
def home(request, response):
    response.text = "I'm Home"


@app.route("/about")
def home(request, response):
    response.text = "I'm moving about in this space."


@app.route("/country/{name}")
def country_detail(request, response, name):
    response.text = f"This country is called {name}"


@app.route("/country")
def country_list(request, response):
    response.text = "All countries"
