'''
Created on May 6, 2018

@author: nopri
'''

from flask_restful import Resource
from dao.AgendaDao import AgendaDao

class Agendas(Resource):
    def get(self):
        agendaDao = AgendaDao()
        result = agendaDao.GetAllAgenda()
        