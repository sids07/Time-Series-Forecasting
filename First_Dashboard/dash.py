from flask import Flask, render_template
from plot import create_plot

app = Flask(__name__)

@app.route("/")
def index():
    bar= create_plot()
    return render_template("index.html",grapJSON=grapJSON)

if __name__ =="__main__":
    app.debug = True 
    app.run()