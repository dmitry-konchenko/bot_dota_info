from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class WardsForm(FlaskForm):
    name_of_map_piece = StringField('Название области карты', validators=[DataRequired()])
    side = StringField('Сторона', validators=[DataRequired()])
    folder_path = StringField('Путь к папке с картинками', validators=[DataRequired()])
