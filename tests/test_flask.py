from core.flask_app import app


def test_home():
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200


def test_database_page():
    client = app.test_client()

    response = client.get("/database")
    assert response.status_code in [200, 302]