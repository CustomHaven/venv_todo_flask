from flask import Flask, render_template, request
from forms import TodoForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

todos = ["Learn Flask", "Setup venv", "Build a cool app"]

@app.route("/", methods=["GET", "POST"])
def index():
    todo_form = TodoForm()
    if "todo" in request.form and todo_form.validate_on_submit():
        todos.append(request.form["todo"])
    return render_template("index.html", todos=todos, template_form=todo_form)