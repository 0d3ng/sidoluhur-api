'''
Created on May 6, 2018

@author: nopri
'''

from flask import Flask
from flask_restful import Api
from resources.Agendas import Agendas
from util.LogUtil import LogUtil

app = Flask(__name__)
api = Api(app)

api.add_resource(Agendas,'/Agendas')

if __name__ == '__main__':
    LogUtil.setup_logging()
    app.run(port=5002,debug='on')