from flask import Flask

app = Flask("test_app")

@app.route('/')
def index():
    return "<h1>Success!</h1>"

if __name__ == "__main__":
    app.run()