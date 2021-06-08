from flask_wtf import FlaskForm
from wtforms.fields import FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired

class UploadArquivo(FlaskForm):
    sobeArquivo = FileField('ARQUIVO', validators=[FileRequired(message="Voce precisa escolher um arquivo pra upar")])
    submit = SubmitField('Enviar')
