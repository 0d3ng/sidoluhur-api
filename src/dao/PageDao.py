'''
Created on May 12, 2018

@author: nopri
'''
from util.Database import Database
import logging

logger = logging.getLogger(__name__)

class PageDao(Database):
    '''
    provide information about page
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(PageDao, self).__init__()
        
    def GetAllPages(self):
        '''
        Get all categories
        @return: List of news
        '''
        query = "SELECT id_halaman,judul,judul_seo,isi_halaman,DATE_FORMAT(tanggal,'%%Y-%%m-%%d') AS tanggal,gambar FROM halamanstatis ORDER BY judul"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e