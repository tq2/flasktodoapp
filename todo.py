import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", "sqlite:///todo.db")
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/complete/<string:id>", methods=["DELETE"])
def completeTodo(id):
    todo = Todo.query.filter_by(id=id).first()

    todo.complete = not todo.complete

    with db.session.begin():
        db.session.add(todo)
    return redirect(url_for("index"))

@app.route("/add", methods = ["POST"])
def addTodo():
    title = request.form.get("title").strip()
    if not title:
        return redirect(url_for("index"))

    newtodo = Todo(title = title, complete=False)
    with db.session.begin():
        db.session.add(newtodo)
    return redirect(url_for("index"))

@app.route("/delete/<string:id>", methods=["DELETE"])
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    with db.session.begin():
        db.session.delete(todo)
    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
