from flask import Flask
from waitress import serve

app = Flask(__name__)

STUDENT_ID = 11


@app.route(f'/api/v1/hello-world-{STUDENT_ID}')
def hello_world():
    return f"Hello world {STUDENT_ID}", 200


if __name__ == "__main__":
    print("4laba.")
    serve(app, port=5000)
