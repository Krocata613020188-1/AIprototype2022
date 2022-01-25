
from flask import Flask, request ,  render_template,redirect,url_for
import json
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost',user='root',
                             password='',
                             database='testweb')
##webapp
@app.route("/adddata")
def home():
    return render_template("web2.html")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/show")
def show():
    with conn:
        cur = conn.cursor()
        cur.execute("select * from testdb1")
        rows = cur.fetchall()
    return render_template("connect.html",datas = rows)

@app.route("/insert",methods = ['POST'])
def insert():
    if request.method =="POST":
        car_id = request.form['car_id']
        Sname = request.form['Sname']
        insurance = request.form['insurance']
        
        with conn.cursor() as cursor:
            sql = "Insert into `testdb1` (`car_id`,`Sname`,`insurance`) values(%s,%s,%s)"
            cursor.execute(sql,(car_id,Sname,insurance))
            conn.commit()
        return redirect(url_for('show'))



if __name__ == "__main__":
    app.run()# host ='0.0.0.0',port=5001 
