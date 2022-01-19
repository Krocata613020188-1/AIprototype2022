from flask import Flask, request ,  render_template
import json

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
@app.route("/home")
def home():
    return render_template("home.html",name = 'Camp')

if __name__ == "__main__":
    app.run()# host ='0.0.0.0',port=5001 
