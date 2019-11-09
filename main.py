import os
import csv
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQL_DB']
mysql = MySQL(app)

@app.route("/")
def index():
    return "<h1>spinne!"

@app.route("/see")
def see():
    return os.environ['MYSQL_USER']

# @app.route("/run")
# def run():
    # query = "SELECT * from indicadores where indicador1 is not null and indicador2 is not null"
    # mycursor.execute(query)
    # row = mycursor.fetchone()
    # colunas = ('id', 'cd_orgao', 'nr_licitacao', 'ano_licitacao', 'vl_licitacao', 'indicador1', 'indicador2')
    # with open('tmp/indicadores.csv', 'a') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerow(colunas)
    #     while row is not None:
    #         writer.writerow(row)
    #         row = mycursor.fetchone()
    # csvFile.close()

# @app.route("/run")
# def licitacoes(): 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)