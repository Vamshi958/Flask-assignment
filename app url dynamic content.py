from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route("/")

def cal():
    return render_template("index1.html")

@app.route("/add",methods=["POST"])

def index():
    ad = request.form["Add"]
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    
    if (ad == "Add"):
        addition = num1 + num2
        return f"addition is :{addition}"

    else:
        return "invalid"

if __name__=="__main__":
    app.run(host="0.0.0.0",port = 5003)



