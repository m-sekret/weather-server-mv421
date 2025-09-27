from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello students"

if __name__ == "__main__":
    # Порт вказується через змінну середовища для Azure
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
