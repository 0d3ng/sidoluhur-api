'''
Created on May 5, 2018

@author: nopri
'''

from util.Database import Database
import logging

logger = logging.getLogger(__name__)

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
        query = "SELECT id_agenda,username,tema,tema_seo,isi_agenda,tempat,pengirim,DATE_FORMAT(tgl_mulai,'%Y-%m-%d') AS tgl_mulai,DATE_FORMAT(tgl_selesai,'%Y-%m-%d') AS tgl_selesai,DATE_FORMAT(tgl_posting,'%Y-%m-%d') AS tgl_posting,jam,gambar FROM agenda"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e
    
    def GetAgendaById(self,id_agenda):
        '''
        Get all agenda
        @return: List of agenda
        '''
        query = "SELECT id_agenda,username,tema,tema_seo,isi_agenda,tempat,pengirim,DATE_FORMAT(tgl_mulai,'%%Y-%%m-%%d') AS tgl_mulai,DATE_FORMAT(tgl_selesai,'%%Y-%%m-%%d') AS tgl_selesai,DATE_FORMAT(tgl_posting,'%%Y-%%m-%%d') AS tgl_posting,jam,gambar FROM agenda WHERE id_agenda=%s"
        logger.info(query)
        try:
            return self.SelectOne(query, id_agenda)
        except Exception as e:
            raise e
        
    def GetAgendaLimit(self,limit):
        '''
        Get all agenda
        @return: List of agenda
        '''
        query = "SELECT id_agenda,username,tema,tema_seo,isi_agenda,tempat,pengirim,DATE_FORMAT(tgl_mulai,'%%Y-%%m-%%d') AS tgl_mulai,DATE_FORMAT(tgl_selesai,'%%Y-%%m-%%d') AS tgl_selesai,DATE_FORMAT(tgl_posting,'%%Y-%%m-%%d') AS tgl_posting,jam,gambar FROM agenda ORDER BY id_agenda DESC LIMIT %s"
        logger.info(query)
        try:
            return self.SelectParams(query, limit)
        except Exception as e:
            raise e
        
    def GetAgendaTwoLimit(self,limit):
        '''
        Get all agenda
        @return: List of agenda
        '''
        query = "SELECT id_agenda,username,tema,tema_seo,isi_agenda,tempat,pengirim,DATE_FORMAT(tgl_mulai,'%%Y-%%m-%%d') AS tgl_mulai,DATE_FORMAT(tgl_selesai,'%%Y-%%m-%%d') AS tgl_selesai,DATE_FORMAT(tgl_posting,'%%Y-%%m-%%d') AS tgl_posting,jam,gambar FROM agenda ORDER BY id_agenda DESC LIMIT %s,%s"
        logger.info(query)
        try:
            return self.SelectParams(query, limit)
        except Exception as e:
            raise e        
    
if __name__ == '__main__':
    agendaDao = AgendaDao()
    result = agendaDao.GetAllAgenda()
    print(result)