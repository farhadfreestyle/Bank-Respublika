from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/bank-respublika'
app.config['SECRET_KEY'] = 'my_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from controllers import *
from extensions import *
from forms import *

from models import *


if __name__ == 'main':
    app.init_app(db)
    app.init_app(migrate)
    app.config(port = 5000)


admin = Admin(app)

admin.add_view(ModelView(Card, db.session))

admin.add_view(ModelView(Card_user, db.session))

admin.add_view(ModelView(Campaign, db.session))

