from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html" )
@app.route("/greed")
def greed():
    name = request.args.get("name","world")
    return render_template("greed.html" ,name=name)
