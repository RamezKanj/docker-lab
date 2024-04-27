import pytest
from app import app, db, User

@pytest.fixture
def client():
    # Set up a test client for the Flask app
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
        yield client  # Provide the test client to the test cases
        db.session.remove()  # Remove the session
        db.drop_all()  # Drop all tables

def test_test_route(client):
    # Test the test route
    response = client.get('/test')
    assert response.status_code == 200
    assert response.json == {'message': 'The server is running'}

def test_create_user(client):
    # Test creating a user
    user_data = {'name': 'John Doe', 'email': 'john@example.com'}
    response = client.post('/api/flask/users', json=user_data)
    assert response.status_code == 201
    assert response.json['name'] == user_data['name']
    assert response.json['email'] == user_data['email']


def test_get_users(client):
    # Test getting all users
    with app.app_context():
        user1 = User(name='Alice', email='alice@example.com')
        user2 = User(name='Bob', email='bob@example.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        response = client.get('/api/flask/users')
        assert response.status_code == 200
        assert len(response.json) == 2

        # Access user attributes within the same context
        users_data = response.json
        assert users_data[0]['name'] == user1.name
        assert users_data[1]['name'] == user2.name

