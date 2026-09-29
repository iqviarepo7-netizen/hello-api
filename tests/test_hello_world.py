from app.main import start

def test_greeting_return():
    assert start() == "hello world"
