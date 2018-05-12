'''
Created on May 12, 2018

@author: nopri
'''
from util.Database import Database
import logging

logger = logging.getLogger(__name__)

class CategoryDao(Database):
    '''
    class provide information about category of contents
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(CategoryDao, self).__init__()
        
    def GetAllCategories(self):
        '''
        Get all categories
        @return: List of news
        '''
        query = "SELECT id_kategori,nama_kategori,kategori_seo,aktif FROM kategori ORDER BY nama_kategori"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e