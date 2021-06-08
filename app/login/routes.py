from app import login_user, render_template, redirect, url_for, login_required, current_user, request, logout_user, login_manager, Mail, Message, generate_password_hash, Blueprint, flash, session, timedelta, jwt, datetime, api
from app.login.forms import LoginForm, Recuperar, CadastroUsuario
from app.models.tables import Usuario, db
import random
import string

login = Blueprint("login", __name__, template_folder='templates', url_prefix='/login')

login_manager.login_view = "login.index"
login_manager.login_message = "Por favor se autenticar antes de acessar o sistema!!!"
login_manager.login_message_category = "info"
login_manager.refresh_view = "relogin"
login_manager.needs_refresh_message = (u"Para proteger sua conta, por favor reautentique para acessar a pagina")
login_manager.needs_refresh_message_category = "info"


@login.before_request
def depois_requisicao():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@login.route('/recuperar', methods=["GET", "POST"])
def recuperar():
    forms = Recuperar()
    if forms.validate_on_submit():
        print(forms.email.data)
        email = Usuario.query.filter_by(email=forms.email.data).first()
        if email is not None:
            token = jwt.encode({'usuario': email, 'exp': datetime.utcnow() + datetime.timedelta(hours=1), app.config["SECRET_KEY"], algorithm='HS256'})
            print(token)
            email.senha = token
            print("EMAIL VINDO DO BANCO {}".format(email))
            msg = Message("Ola isso eh um teste", sender=app.config["MAIL_USERNAME"], recipients=[email.email])
            msg.body = "Para trocar sua senha clique aqui {}{}".format("http://127.0.0.1:59000/alterarSenha?token=", token)
            mail.send(msg)
            flash("Email disparado com sucesso!!!", "info")
            return redirect(url_for('login.index'))
        else:
            flash("Email nao cadastrado na base de dados", "warning")
            return redirect(url_for("login.index"))
    return render_template("recuperar.html", form=forms)


@login.route('alterarSenha', methods=["GET", "POST"])
def recuperarAlterar():
    forms = LoginForm()
    if forms.validate_on_submit():
        email = Usuario.query.filter_by(email=forms.email.data).first()
        if email is not None:
            email.senha = generate_password_hash(forms.senha.data)
            # db.session.commit()
            flash("Senha alterada com sucesso!!!", "success")
            return redirect(url_for("login.index"))
        else:
            flash("Erro ao alterar a senha", "warning")
            return redirect(url_for("login.index"))
    return render_template("recuperarAlterar.html", form=forms)


@login.route("/register", methods=["GET", "POST"])
def register():
    formRegistroPessoa = CadastroUsuario()
    print(formRegistroPessoa.nome.data)
    if formRegistroPessoa.validate_on_submit():
        user = Usuario(formRegistroPessoa.nome.data, formRegistroPessoa.email.data, formRegistroPessoa.senha.data, formRegistroPessoa.sexo.data, formRegistroPessoa.cpf.data, formRegistroPessoa.tel.data, formRegistroPessoa.dataNasc.data)
        db.session.add(user)
        db.session.commit()
        flash("Usuario cadastrado com sucesso!!!", "success")
        return redirect(url_for("login.login"))
