import os
import csv
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# mydb = mysql.connector.connect(
#   host=os.environ['MYSQL_HOST'],
#   user=os.environ['MYSQL_USER'],
#   passwd=os.environ['MYSQL_PASSWORD'],
#   database=os.environ['MYSQL_DB']
# )

@app.route("/")
@cross_origin()
def index():
    return "<h1>spinne!"

@app.route("/see")
def see():
    return os.environ['MYSQL_USER']

# @app.route("/licitacoes")
# def licitacoes():
    # mycursor = mydb.cursor()
    # query = "SELECT id, ano_licitacao, cd_orgao, cd_tipo_modalidade, nr_licitacao, nr_processo, ano_processo FROM licitacoes order by 1,2,3,4,5,6,7"
    # mycursor.execute(query)
    # row = mycursor.fetchone()
    # while row is not None:
    #     print(row)
    #     row = mycursor.fetchone()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)