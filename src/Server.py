'''
Created on May 6, 2018

@author: nopri
'''

from flask import Flask
from flask_restful import Api
from dao.AgendaDao import AgendaDao
from dao.ArtikelDao import ArtikelDao

app = Flask(__name__)
api = Api(app)

api.add_resource(AgendaDao,'/Agendas')
api.add_resource(ArtikelDao,'/Articles')

if __name__ == '__main__':
    app.run(port=5002)