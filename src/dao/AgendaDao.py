'''
Created on May 5, 2018

@author: nopri
'''

from util.Database import Database
import logging
import json

logger = logging.getLogger('AgendaDao')

class AgendaDao(Database):
    '''
    class to provide information about agenda
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(AgendaDao, self).__init__()
        
    def GetAllAgenda(self):
        '''
        Get all agenda
        @return: List of agenda
        '''
        query = "SELECT id_agenda,username,tema,tema_seo,isi_agenda,tempat,pengirim,tgl_mulai,tgl_selesai,tgl_posting,jam,gambar FROM agenda"
        logger.info(query)
        return self.SelectAll(query)
    
if __name__ == '__main__':
    agendaDao = AgendaDao()
    result = agendaDao.GetAllAgenda()
    listAgendas = []
    for row in result:
        listAgendas.append(row)
    print(json.dumps(listAgendas))