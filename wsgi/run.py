from flask import Flask

app = Flask(__name__)


# Create our index or root / route
@app.route("/")
@app.route("/index")
def index():
    return "Python - Hello World! v1.1 - Hi Candace"

@app.route("/nick")
def nick():
    return "Nick's secret route"

if __name__ == "__main__":
    app.run()  # debug="True")
