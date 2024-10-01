from app import db, create_app
import pytest

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables within the context
        yield app
        db.session.remove()  # Cleanup session objects
        #db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def usuario(app):
    from app.models.usuario import Usuario
    usuario = Usuario(nameUser="test_user", passwordUser="test_password")
    db.session.add(usuario)
    db.session.commit()  # Commit changes within the context
    yield usuario

