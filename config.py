DEBUG = True

UPLOAD_FOLDER = '/static'
MAX_CONTENT_PATH = 16 * 1000 * 1000 * 1000
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'mp4', 'mpeg'}

SQLALCHEMY_DATABASE_URI = "mysql+pymsql://root@''@localhost:3306/filmes"

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "pythonFilmes"

MAIL_SERVER = 'smtp-mail.outlook.com'
MAIL_PORT = 587
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_USER_TLS = True
MAIL_USER_SSL = False
