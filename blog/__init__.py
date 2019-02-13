from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()#add added functionality to our db models
login_manager.login_view = 'users.login'#route to go to before accessing login_required route
login_manager.login_message_category = 'danger' # custom flash message

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from blog.users.routes import users #we now just import the blueprint
    from blog.posts.routes import posts
    from blog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main) 

    return app