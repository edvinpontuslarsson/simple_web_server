from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<a href='/spanish-inquisition'>I didn't expect the Spanish Inquisition</a>"

@app.route("/spanish-inquisition")
def spanish_inquisition():
    return '<a href="/"><h1>Nobody expects the Spanish Inquisition!</h1></a>'

if __name__ == "__main__":
    app.run(debug=True, host="localhost")

