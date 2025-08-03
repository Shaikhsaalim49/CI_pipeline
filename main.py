from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Python App via CI/CD Pipeline!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# tests/test_main.py
def test_dummy():
    assert True
