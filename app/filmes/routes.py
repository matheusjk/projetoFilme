from app import Flask, render_template, Blueprint, redirect, url_for, request, flash, login_user, login_required, current_user, login_manager, os, secure_filename, api
from app.filmes.forms import UploadArquivo
# from app.models.tables import Filmes, db
# os.chdir('/home/matheus/Documentos/projetoFilmes/app/static/filmesSeries')

filmes = Blueprint('filmes', __name__, template_folder='templates', url_prefix='/filmes')

@filmes.route("/")
def teste():
    form = UploadArquivo()
    print(os.listdir(os.getcwd()))
    video =  [url for url in os.listdir(api.config['UPLOAD_FOLDER']) if "mp4" in url]
    # print("URL {}".format(video))
    return render_template('index.html', form=form, filmesPath=video)

def extensaoArquivo(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in api.config['ALLOWED_EXTENSIONS']

@filmes.route('/upload', methods=['GET', 'POST'])
def uploadFile():
    form = UploadArquivo()
    if form.validate_on_submit():
        # print(form.sobeArquivo.data)
        print(dir(form.sobeArquivo.data), form.sobeArquivo, form.sobeArquivo.data.filename)
        if extensaoArquivo(form.sobeArquivo.data.filename):
            # print(api.config['UPLOAD_FOLDER'])
            filename = secure_filename(form.sobeArquivo.data.filename)
            file_path = os.path.join(api.config['UPLOAD_FOLDER'], filename)
            form.sobeArquivo.data.save(file_path)
            flash('ARQUIVO UPADO COM SUCESSO!!!', 'info')
            return redirect(url_for('filmes.teste'))
    return redirect(url_for('filmes.teste'))

# @filmes.errorhandler(404)
# def naoEncontrado():
#     return render_template('error.html'), 404
