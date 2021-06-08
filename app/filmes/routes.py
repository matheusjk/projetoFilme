from app import Flask, render_template, Blueprint, redirect, url_for, request, flash, login_user, login_required, current_user, login_manager, os, secure_filename, app
from app.filmes.forms import UploadArquivo 
# from app.models.tables import Filmes, db

os.chdir('/home/matheus/Documentos/projetoFilmes/app/static')

filmes = Blueprint('filmes', __name__, template_folder='templates', url_prefix='/filmes')



@filmes.route("/")
def teste():
    form = UploadArquivo()
    print(os.listdir(os.getcwd()))
    video =  [url for url in os.listdir(os.getcwd()) if "mp4" in url]
    print("URL {}".format(video))
    return render_template('index.html', form=form, filmesPath=os.listdir(os.getcwd()))  

def extensaoArquivo(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@filmes.route('/upload', methods=['GET', 'POST'])
def uploadFile():
    form = UploadArquivo()
    if form.validate_on_submit():
        print(form.sobeArquivo.data)
        if extensaoArquivo(form.sobeArquivo.filename):
            filename = secure_filename(form.sobeArquivo.file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash('ARQUIVO UPADO COM SUCESSO!!!', 'info')
            return redirect(url_for('teste'))
    return redirect(url_for('teste'))

# @filmes.errorhandler(404)
# def naoEncontrado():
#     return render_template('error.html'), 404