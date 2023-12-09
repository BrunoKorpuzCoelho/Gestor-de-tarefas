from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # Servidor
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///c:/Users/KorpuZ/Desktop/Gestor de tarefas VSC/tarefas.db"
db = SQLAlchemy(app) #Cursor


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

app.run()