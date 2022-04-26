from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from  datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
  sno=db.Column(db.Integer, primary_key=True)
  title=db.Column(db.String(200),nullable=False)
  desc=db.Column(db.String(500),nullable=False)
  date_created=db.Column(db.DateTime, default=datetime.utcnow())

  def __str__(self):
    return f"{self.sno} - {self.title}"

@app.route("/",methods=["GET", "POST"])
def hello_world():
  if request.method =="POST":
    title=request.form['title']
    desc=request.form['desc']
    todo=Todo(title=title,desc=desc)
    db.session.add(todo)
    db.session.commit()
  allTodo=Todo.query.all()
  return render_template('index.html',allTodo=allTodo)

@app.route("/show")
def showdata():
  allTodo=Todo.query.all()
  return "<h1>Hi, Chikku How are you</h1>"

@app.route("/update")
def update():
  allTodo=Todo.query.all()
  return "<h1>Hi, Chikku How are you</h1>"

@app.route('/delete/<int:sno>')
def delete(sno):
  todo=Todo.query.filter_by(sno=sno).first()
  db.session.delete(todo)
  db.session.commit()
  return redirect("/")


if __name__=="__main__":
  app.run(debug=True,port=8080)