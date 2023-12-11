from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__) # Servidor
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\KorpuZ\\Desktop\\Gestor de tarefas VSC\\database\\tarefas.db"
db = SQLAlchemy(app) # Cursor

class Tarefa(db.Model):
    __tablename__ = "tarefas"
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(200))
    feita = db.Column(db.Boolean)




@app.route("/")
def home():
    todas_as_tarefas = Tarefa.query.all()
    return render_template("index.html", lista_de_tarefas = todas_as_tarefas)


@app.route("/criar-tarefa", methods=["POST"])
def criar():
    conteudo_tarefa = request.form["conteudo_tarefa"] 
    tarefa = Tarefa(conteudo=conteudo_tarefa, feita=False)
    db.session.add(tarefa)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/eliminar-tarefa/<id>")
def eliminar(id):
    tarefa = Tarefa.query.get(int(id))
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarefa-feita/<id>")
def feita(id):
    tarefa = Tarefa.query.filter_by(id = int(id)).first()
    tarefa.feita = not tarefa.feita
    db.session.commit()
    return redirect(url_for("home"))





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()

    app.run()





