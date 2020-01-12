from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
app=Flask(__name__)
app.config['SECRET_KEY']='1234'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='PIZZA NAPOLI', template_mode='bootstrap3')
db=SQLAlchemy(app)
login_manager = LoginManager(app)


from ProiectPa.models import User , Menu , Ingredients , Post

admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Menu,db.session))
admin.add_view(ModelView(Ingredients,db.session))
admin.add_view(ModelView(Post,db.session))
from ProiectPa import routes