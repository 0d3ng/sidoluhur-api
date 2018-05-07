'''
Created on May 6, 2018

@author: nopri
'''

from flask_restful import Resource
from dao.AgendaDao import AgendaDao
from flask_jsonpify import jsonify
import logging

class Agendas(Resource):
    
    logger = logging.getLogger('Agendas')
    
    def get(self):
        agendaDao = AgendaDao()
        result = agendaDao.GetAllAgenda()
        agendas = []
        for row in result:
            agendas.append(row)
        return jsonify(agendas)
    