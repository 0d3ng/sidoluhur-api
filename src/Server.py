'''
Created on May 6, 2018

@author: nopri
'''

from flask import Flask
from flask_restful import Api
from util.LogUtil import LogUtil
from resources.Agenda import Agenda
from resources.Artikel import Artikel

app = Flask(__name__)
api = Api(app)

#Agendas
api.add_resource(Agenda,'/sidoluhur/api/v1.0/agendas')

#Article
api.add_resource(Artikel,'/sidoluhur/api/v1.0/articles')

if __name__ == '__main__':
    LogUtil.setup_logging()
    app.run(port=5002,debug=True)