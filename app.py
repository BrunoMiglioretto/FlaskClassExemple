from flask import Flask, render_template, request, url_for, redirect
from admin.admin import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")


links = [
    ["/orders", "Orders"],
    ["/clients", "Clients"],
    ["/employees", "Employees"],
    ["/create_order", "Create order"]
]
orders_mock = []
clients_mock = []


@app.route("/")
def index():
    return render_template("index.html", links=links)


@app.route("/order_list")
def order_list():
    return render_template(
        "order-list.html",
        links=links,
        orders=orders_mock,
    )


@app.route("/order_create", methods=["GET", "POST"])
def order_create():
    if request.method == "GET":
        return render_template("create_orders.html")
    else:
        name = request.form.get("name")
        ticket_number = request.form.get("ticket_number")

        orders_mock.append(name)
        print(orders_mock)
        return redirect(url_for("create_order"))


@app.route("/client_list")
def client_list():
    return render_template("clients.html", links=links, clients=clients_mock)


@app.route("/client_create", methods=["GET", "POST"])
def client_create():
    if request.method == "GET":
        return render_template("client-create.html")


@app.route("/employee_list")
def employee_list():
    return render_template("employees.html")


if __name__ == "__main__":
    app.run()
