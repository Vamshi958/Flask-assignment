from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route("/")
def show():
    return render_template("indexform.html")

@app.route("/display",methods=["POST"])

def display():
    username = request.form["username"]
    email = request.form["email"]
    message = request.form["message"]
    
    return render_template("user_DATADISPLAY.HTML",username=username,email=email, message=message)

if __name__=="__main__":
    app.run(host="0.0.0.0",port = 5004)



