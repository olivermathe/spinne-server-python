import os
import csv
from flask import Flask
from flask_cors import CORS, cross_origin

# import csv
# from filtros import *

# import hdbscan
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

import mysql.connector

mydb = mysql.connector.connect(
  host=os.environ['MYSQL_HOST'],
  user=os.environ['MYSQL_USER'],
  passwd=os.environ['MYSQL_PASSWORD'],
  database=os.environ['MYSQL_DB']
)

mycursor = mydb.cursor()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def index():
    return "<h1>spinne!"

@app.route("/see")
@cross_origin()
def see():
    return os.environ['MYSQL_USER']

@app.route("/run")
@cross_origin()
def run():

    query = "SELECT * from indicadores where indicador1 is not null and indicador2 is not null"

    print(query)

    mycursor.execute(query)

    row = mycursor.fetchone()
    colunas = ('id', 'cd_orgao', 'nr_licitacao', 'ano_licitacao', 'vl_licitacao', 'indicador1', 'indicador2')
   
    with open('indicadores.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(colunas)
        while row is not None:
            print("ROW \/")
            print(row)
            writer.writerow(row)
            row = mycursor.fetchone()
    csvFile.close()

    # df_csv = pd.read_csv('indicadores2-07-11.csv')[['id','vl_licitacao','indicador1','indicador2']]
    # df_csv[:5]
    # df=df_csv[['vl_licitacao','indicador1','indicador2']]
    # from sklearn import preprocessing

    # df=df_csv[['vl_licitacao','indicador1','indicador2']]
    # min_max_scaler = preprocessing.MinMaxScaler()
    # scaled_array = min_max_scaler.fit_transform(df.values.astype(float))
    # df_normalized = pd.DataFrame(scaled_array)
    # df_normalized[:5]

    # data = df_normalized.to_numpy()
    # clusterer = hdbscan.HDBSCAN(min_cluster_size=35, prediction_data=True).fit(data)

    # # Visualizando os dados após clusterização
    # from sklearn.manifold import TSNE
    # projection = TSNE().fit_transform(data)

    # color_palette = sns.color_palette('Paired', 12)
    # cluster_colors = [color_palette[x] if x >= 0
    #                 else (0.5, 0.5, 0.5)
    #                 for x in clusterer.labels_]
    # cluster_member_colors = [sns.desaturate(x, p) for x, p in
    #                         zip(cluster_colors, clusterer.probabilities_)]
    # plt.scatter(*projection.T, s=50, linewidth=0, c=cluster_member_colors, alpha=0.25)

    # df_clusterized = pd.DataFrame({'Id': df_csv['id'] ,'Grupo': clusterer.labels_, 'Prob': clusterer.probabilities_})
    # df_clusterized.to_csv("clusterized.csv")







    # contador = 0
    # # inicia leitura do arquivo
    # arquivo = open('tmp/clusterized.csv')
    # linhas = csv.reader(arquivo)

    # # le primeira linha (cabecalho)
    # colunas = next(linhas)

    # # pega posicao dos campos
    # idd = colunas.index('Id')
    # grupo = colunas.index('Grupo')
    # prob = colunas.index('Prob')

    # def insert_linha_cluster(linha):

    #     sql = "INSERT INTO licitacao_cluster (" \
    #             "id, " \
    #             "grupo, " \
    #             "prob) " \
    #             "VALUES (" \
    #             " " + linha[idd] + ", " \
    #             " " + linha[grupo] + ", " \
    #             " '" + linha[prob] + "'); " \

    #     print sql

    #     mycursor.execute(sql)

    #     mydb.commit()

    # # percorre linhas
    # for linha in linhas:
    #     insert_linha_cluster(linha)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)