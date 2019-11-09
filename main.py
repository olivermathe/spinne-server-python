import os
import csv
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="spinne.cjbqzqzg45ji.us-east-2.rds.amazonaws.com",
#   user="spinne",
#   passwd="Spinn32019",
#   database="spinnedb"
# )

# mycursor = mydb.cursor()
# query = "SELECT * from indicadores where indicador1 is not null and indicador2 is not null"
# mycursor.execute(query)
# row = mycursor.fetchone()

# while row is not None:
#     writer.writerow(row)
#     row = mycursor.fetchone()




# app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
# app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
# app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
# app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
# mysql = MySQL(app)

@app.route("/")
def index():
    return "<h1>spinne!"

@app.route("/see")
def see():
    return os.environ['MYSQL_USER']

# @app.route("/licitacoes")
# def licitacoes():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT id, ano_licitacao, cd_orgao, cd_tipo_modalidade, nr_licitacao, nr_processo, ano_processo FROM licitacoes order by 1,2,3,4,5,6,7''')
#     row_headers=[x[0] for x in cur.description] #this will extract row headers
#     rv = cur.fetchall()
#     json_data=[]
#     for result in rv:
#         json_data.append(dict(zip(row_headers,result)))
#     return json.dumps(json_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)