import app


def test_hello():
    res = app.app.test_client().get("/hello")
    assert res.status_code == 200
    assert res.data == b"Hello World"

def test_home():
    res = app.app.test_client().get("/")
    assert res.status_code == 200
    assert res.data == b"Hello I am Huzail"

def test_goo():
    res = app.app.test_client().get("/goo")
    assert res.status_code == 404

