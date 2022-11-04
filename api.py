from flask import Flask

app = Flask(__name__)

@app.route("/profile")
def myProfile():
    response_body = {
        "name": "Evan Zhao",
        "about": "I'm currently in the process of learning how to connect my backend to React!"
    }
    return response_body

if __name__ == "__main__":
    app.run()