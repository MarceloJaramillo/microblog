from flask import Flask
from config import Config
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#inicializar la aplicacion app con la configuracion Config y la base de datos db
app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
#configuracion para migraciones
migrate = Migrate(app, db, compare_type=True)
#importar las rutas y modelos por si queremos usarlos
from app import models, topRoutes

from app.routes.login_bp import login_bp
from app.routes.profile_bp import profile_bp

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(profile_bp, url_prefix="/profile")
#podemos crear las tablas aqui si no queremos hacerlo manualmente
#db.create_all()