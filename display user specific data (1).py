from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route("/")
def show():
    return render_template("files.html")

@app.route("/upload",methods=["POST"])

def file():
   
    file1 = request.files["file"]
    
    return render_template("displayfile.html",filename=file1.filename)

if __name__=="__main__":
    app.run(host="0.0.0.0",port = 5004)



