from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/orders")
def orders():
    return render_template(
        "orders.html",
        orders=[
            "Salad",
            "Some fruit",
            "Some garbage",
            "Some fastfood",
            "Whatever",
        ],
    )


@app.route("/clients")
def clients():
    return render_template("clients.html")


@app.route("/employees")
def employees():
    return render_template("employees.html")


if __name__ == "__main__":
    app.run()
