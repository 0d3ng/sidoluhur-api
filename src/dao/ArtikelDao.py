'''
Created on May 5, 2018

@author: nopri
'''
from util.Database import Database
import logging

logger = logging.getLogger('AgendaDao')


class ArtikelDao(Database):
    '''
    class to provide information about agenda
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArtikelDao, self).__init__()
        
    def GetAllArtikel(self):
        '''
        Get all agenda
        @return: List of agenda
        '''
        query = "SELECT id_artikel,username,judul_artikel,artikel_seo,isi_artikel,gambar,publish,hari,tanggal,jam,dibaca,tag_seo,buletin FROM artikel"
        logger.info(query)
        return self.SelectAll(query)
    
if __name__ == '__main__':
    artikeDao = ArtikelDao()
    print(artikeDao.GetAllArtikel())  