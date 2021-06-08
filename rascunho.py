from flask import Flask, render_template, Blueprint
from app import filmes
import os

app = Flask(__name__)
app.register_blueprint(filmes)
app.secret_key = "testando"

app.config['UPLOAD_FOLDER']
app.config['MAX_CONTENT_PATH']

os.chdir('/home/matheus/Documentos/projetoFilmes/static')

@app.route("/")
def teste():
    print(os.listdir(os.getcwd()))
    video =  [url for url in os.listdir(os.getcwd()) if "mp4" in url or "mpeg" in url]
    print("URL {}".format(video))
    return render_template('index.html', filmesPath=video)  

@app.route('/upload')
def uploadFile():
    if val