'''
Created on May 12, 2018

@author: nopri
'''
from util.Database import Database
import logging

logger = logging.getLogger(__name__)

class GaleryDao(Database):
    '''
    class to provide information about galery
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(GaleryDao, self).__init__()
        
    def GetAllGaleries(self):
        '''
        Get all categories
        @return: List of news
        '''
        query = "SELECT id_galeri,id_album,judul_galeri,galeri_seo,keterangan,foto FROM galeri WHERE id_album !=0"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e
        
    def GetGaleryByAlbum(self,id_album):
        '''
        Get category by album
        @return: List of news
        '''
        query = "SELECT id_galeri,id_album,judul_galeri,galeri_seo,keterangan,foto FROM galeri WHERE id_album !=0 AND id_album=%s"
        logger.info(query)
        try:
            return self.SelectParams(query, id_album)
        except Exception as e:
            raise e