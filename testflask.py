from unicodedata import name
from flask import Flask, request ,  render_template
import json
import pandas as pd

app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello, World!"
    
@app.route("/name")
def hellocamp():
    return "Hello, Camp!"

## api
@app.route('/request',methods = ['POST'])
def request_detail():
    payload = request.data.decode("utf-8")
    inmassage = json.loads(payload)

    print(inmassage)

    json_data = json.dumps({"y":"received"})
    return json_data

##webapp
@app.route("/home",methods = ['POST','GET'])
def home():
    dbpd = pd.read_csv('db.csv')
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        dbpd = dbpd.append({'name':first_name,'lastname':last_name},ignore_index=True)
        dbpd.to_csv('db.csv',index=False)
        return render_template("home.html",name = f"{first_name} {last_name}")

    return render_template("home.html",name = "Camp")

@app.route("/hora",methods = ['POST','GET'])
def hora():
    if request.method == "POST":
        sel = request.form.get("fav_language")
        return render_template("home.html",name = "Camp",item =(sel))

    return render_template("home.html",name = "Camp")




if __name__ == "__main__":
    app.run()# host ='0.0.0.0',port=5001 
