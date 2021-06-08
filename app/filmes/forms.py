from flask_wtf import FlaskForm
from wtforms.fields import FileField, SubmitField
from wtforms.validators import DataRequired

class UploadArquivo(FlaskForm):
    sobeArquivo = FileField('ARQUIVO', validators=[DataRequired(message="Voce precisa escolher um arquivo pra upar")])
    submit = SubmitField('Enviar')