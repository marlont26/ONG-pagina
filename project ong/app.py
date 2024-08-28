from flask import Flask
from app import db
from app.usuario.routes import bp  # Importa el Blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/ong'
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)

# Registra el Blueprint
app.register_blueprint(bp, url_prefix='/usuario')

if __name__ == '__main__':
    app.run(debug=True)