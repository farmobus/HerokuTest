import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<div style='background: #f4f4f4;'>test</div>"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)