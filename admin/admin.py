from flask import Blueprint

admin = Blueprint("admin", __name__, static_folder="static", template_folder="template")

@admin.route("/")
def admin_index():
    return "This is my admin module"

