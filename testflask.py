from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
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

if __name__ == "__main__":
    app.run()#host ='0.0.0.0'
