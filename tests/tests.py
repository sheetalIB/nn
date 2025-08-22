from app import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.data == b"Hello, CI/CD with GitHub Actions!"
