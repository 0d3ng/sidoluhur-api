'''
Created on May 6, 2018

@author: nopri
'''

from flask_restful import Resource
from dao.AgendaDao import AgendaDao
from flask_jsonpify import jsonify
import logging

class Agenda(Resource):
    
    logger = logging.getLogger('Agenda')
    
    def get(self):
        agendaDao = AgendaDao()
        result = agendaDao.GetAllAgenda()
        return jsonify({'agendas':result})
    