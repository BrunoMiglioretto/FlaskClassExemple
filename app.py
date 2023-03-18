from flask import Flask, render_template, request, url_for
from faker import Faker

app = Flask(__name__)

faker = Faker()

links = [
    ["/orders", "Orders"],
    ["/clients", "Clients"],
    ["/employees", "Employees"],
]
orders_mock = [
    "Salad",
    "Some fruit",
    "Some garbage",
    "Some fastfood",
    "Whatever",
]

clients_mock = [faker.name() for _ in range(5)]


@app.route("/")
def index():
    return render_template("index.html", links=links)


@app.route("/orders")
def orders():
    return render_template(
        "orders.html",
        links=links,
        orders=orders_mock,
    )

@app.route("/test")
def test():
    return url_for("orders")


@app.route("/clients")
def clients():
    return render_template("clients.html", links=links, clients=clients_mock)


@app.route("/employees")
def employees():
    return render_template("employees.html")


if __name__ == "__main__":
    app.run()
