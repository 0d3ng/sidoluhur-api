'''
Created on May 12, 2018

@author: nopri
'''
from util.Database import Database
import logging

logger = logging.getLogger(__name__)

class AlbumDao(Database):
    '''
    class to provide information about album photo
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        super(AlbumDao, self).__init__()
        
    def GetAllAlbum(self):
        '''
        Get all album
        @return: List of album
        '''
        query = "SELECT id_album,nama_album,album_seo,gambar,aktif FROM album"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e