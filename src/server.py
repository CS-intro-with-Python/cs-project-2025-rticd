import os
from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

app = Flask(__name__)


port = int(os.environ.get("PORT", "5000"))

print(port)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000))
    deadline = db.Column(DateTime(timezone=False))
    status = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "status": self.status
        }

with app.app_context():
    db.create_all()



@app.route("/")
def root():
    return redirect("/tasks")

@app.route("/tasks")
def tasks():
    tsks = Task.query.all()
    return render_template("tasks_page.html", tasks=[task.to_dict() for task in tsks])


@app.route("/add_task", methods=["POST"])
def add_task():
    title = request.form.get("title")
    description = request.form.get("description")
    deadline = request.form.get("deadline")

    task = Task(
        title=title,
        description = description,
        deadline = deadline,
        status = 1
    )

    try:
        db.session.add(task)
        db.session.commit()
        return redirect("/tasks")
    except Exception:
        db.session.rollback()
        return redirect("/tasks")

    

@app.route("/tasks/new")
def tasks_new():
    return render_template("new_task_form.html")

@app.route("/tasks/edit")
def tasks_edit():
    

app.run(host="0.0.0.0", port=port)