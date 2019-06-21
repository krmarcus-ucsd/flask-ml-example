from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField

class SimilarItemsForm(FlaskForm):
   item_id = TextField("Item Id")
   submit = SubmitField("Find Similar Items")
   similarItems = {}
