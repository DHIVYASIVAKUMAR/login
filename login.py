from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flaskext.mysql import MySQL
from flask_cors import CORS,cross_origin
import sys
import json

mysql = MySQL()
app = Flask(__name__)
CORS(app)
cors=CORS(app,resources={
    r"/*":{
        "origins":'http://localhost:4200',
        "methods":['GET','POST','PUT','DELETE']
    }
})


env = 'dhivya'
port = 5000
if __name__ == "__main__":
    if len(sys.argv) > 1:
        env = sys.argv[1]
        print("env=" + env)
    if len(sys.argv) > 2:
        port = sys.argv[2]
        print("port=" + port)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Vino1@dhiya'
app.config['MYSQL_DATABASE_DB'] = env
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

api = Api(app)

class Admin(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        select_query = "select * from users "
        cursor.execute(select_query)
        rows = cursor.fetchall()
        if len(rows) > 0:
            resp = {'uid': rows[0][0], 'uname': rows[0][1], 'upassword': rows[0][2], 'phonenum': rows[0][3],'log_time': rows[0][4],'dates': rows[0][5]}
#            resp = jsonify(rows)
            return resp

        return {'student': None}, 201
class User(Resource):
    def get(self, phonenum):
        conn = mysql.connect()
        cursor = conn.cursor()
        select_query = "select * from users where  phonenum = " + str(phonenum)
        cursor.execute(select_query)
        rows = cursor.fetchall()
        if len(rows) > 0:
            resp = {'uid': rows[0][0], 'uname': rows[0][1], 'upassword': rows[0][2], 'phonenum': rows[0][3],'log_time': rows[0][4],'dates': rows[0][5]}
#            resp = jsonify(rows)
            return resp

        return {'student': None}, 201


api.add_resource(Admin, '/admin/')
api.add_resource(User, '/user/<string:phonenum>')
app.run(port = port,debug = True)