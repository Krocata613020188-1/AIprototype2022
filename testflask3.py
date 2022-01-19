from flask import Flask, request ,  render_template
import json

app = Flask(__name__)

##webapp
@app.route("/home")
def home():
    return render_template("web2.html")

if __name__ == "__main__":
    app.run(host ='0.0.0.0',port=5001)# host ='0.0.0.0',port=5001 
