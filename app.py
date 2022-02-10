from flask import Flask, g
import sqlite3

DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__

def conectar_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.db = conectar_db()
    
@app.teardown_request
def fim_requisicao(exc):
    g.db.close()
        
        
@app.route("/")
def exibir_posts():
    sql_cmd = """
        SELECT id, titulo, texto 
        FROM entradas ORDER BY id DESC;
    """
    cur = g.db.execute(sql_cmd)
    entradas = []
  
    return str(entradas)
