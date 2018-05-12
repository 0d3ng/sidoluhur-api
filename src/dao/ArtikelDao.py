'''
Created on May 5, 2018

@author: nopri
'''
from util.Database import Database
import logging

logger = logging.getLogger(__name__)


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
        query = "SELECT id_artikel,username,judul_artikel,artikel_seo,isi_artikel,gambar,publish,hari,DATE_FORMAT(tanggal,'%Y-%m-%d') AS tanggal,DATE_FORMAT(jam,'%H:%m:%s') AS jam,dibaca,tag_seo,buletin FROM artikel"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e
        
    def GetArtikelById(self,id_artikel):
        '''
        Get agenda by id
        @return: object of agenda
        '''
        query = "SELECT id_artikel,username,judul_artikel,artikel_seo,isi_artikel,gambar,publish,hari,DATE_FORMAT(tanggal,'%%Y-%%m-%%d') AS tanggal,DATE_FORMAT(jam,'%%H:%%m:%%s') AS jam,dibaca,tag_seo,buletin FROM artikel WHERE id_artikel=%s"
        logger.info(query)
        try:
            return self.SelectOne(query, id_artikel)
        except Exception as e:
            raise e
     
    def GetArtikelPopular(self):
        '''
        Get all agenda
        @return: List of agenda
        '''
        query = "SELECT id_artikel,username,judul_artikel,artikel_seo,isi_artikel,gambar,publish,hari,DATE_FORMAT(tanggal,'%Y-%m-%d') AS tanggal,DATE_FORMAT(jam,'%H:%m:%s') AS jam,dibaca,tag_seo,buletin FROM artikel ORDER BY dibaca DESC"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e   
    
if __name__ == '__main__':
    artikeDao = ArtikelDao()
    print(artikeDao.GetAllArtikel())  