from app import db, login_manager, generate_password_hash, check_password_hash, func, UserMixin, datetime

class Filmes(UserMixin, db.Model):
    __tablename = "filmes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    resenha = db.Column(db.String(100), nullable=False)
    dataLancamento = db.Column(db.DateTime(), nullable=False)

    def __init__(self, titulo, resenha, dataLancamento):
        self.titulo = titulo
        self.resenha = resenha
        self.dataLancamento = dataLancamento


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    dataCriacao = db.Column(db.DateTime(), default=func.localtimestamp(), nullable=False)
    ultimoLogin = db.Column(db.DateTIme, index=False, unique=False, nullable=True)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

    def verifica_senha(self, senhaTemp):
        check_password_hash(self.senha, senhaTemp)
        return generate_password_hash(senhaTemp)

# db.session.remove()
# db.reflect()
# db.drop_all()
db.create_all()
