from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route("/")
def show():
    return render_template("indexform.html")

@app.route("/display",methods=["POST"])

def display():
    ad = request.form["username"]
    num1 = (request.form["email"])
    num2 = (request.form["message"])
    
    return "info received"

if __name__=="__main__":
    app.run(host="0.0.0.0",port = 5004)



