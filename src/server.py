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

with app.app_context():
    db.create_all()


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000))
    deadline = db.Column(DateTime(timezone=True))
    status = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "status": self.status
        }

@app.route("/")
def root():
    return redirect("/tasks")

@app.route("/tasks")
def tasks():
    tsks = Task.query.all()
    return render_template([task.to_dict() for task in tsks])

app.run(host="0.0.0.0", port=port)