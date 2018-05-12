'''
Created on May 12, 2018

@author: nopri
'''
from util.Database import Database
import logging

logger = logging.getLogger(__name__)

class BeritaDao(Database):
    '''
    class to provide information about news
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(BeritaDao, self).__init__()
        
    def GetAllBerita(self):
        '''
        Get all news
        @return: List of news
        '''
        query = "SELECT b.id_berita,b.id_kategori,b.username,b.judul,b.judul_seo,b.headline,b.isi_berita,b.gambar,b.nama_lengkap,b.publish,b.hari,DATE_FORMAT(b.tanggal,'%Y-%m-%d') AS tanggal,DATE_FORMAT(b.jam,'%H:%m:%s') AS jam,b.dibaca,b.tag FROM berita b"
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e
        
    def GetBeritaById(self,id_berita):
        '''
        Get all news
        @return: List of news
        '''
        query = '''SELECT b.id_berita,b.id_kategori,b.username,b.judul,b.judul_seo,b.headline,b.isi_berita,b.gambar,b.nama_lengkap,b.publish,b.hari,DATE_FORMAT(b.tanggal,'%%Y-%%m-%%d') AS tanggal,DATE_FORMAT(b.jam,'%%H:%%m:%%s') AS jam,b.dibaca,b.tag FROM berita b WHERE b.id_berita=%s '''
        logger.info(query)
        try:
            return self.SelectOne(query, id_berita)
        except Exception as e:
            raise e
        
    def GetBeritaLimit(self,limit):
        '''
        Get all news
        @return: List of news
        '''
        query = '''SELECT b.id_berita,b.id_kategori,b.username,b.judul,b.judul_seo,b.headline,b.isi_berita,b.gambar,b.nama_lengkap,b.publish,b.hari,DATE_FORMAT(b.tanggal,'%%Y-%%m-%%d') AS tanggal,DATE_FORMAT(b.jam,'%%H:%%m:%%s') AS jam,b.dibaca,b.tag FROM berita b ORDER BY b.id_berita DESC LIMIT %s'''
        logger.info(query)
        try:
            return self.SelectParams(query, limit)
        except Exception as e:
            raise e
        
    def GetBeritaPopular(self):
        '''
        Get popular news limit 5, most read
        @return: List of news
        '''
        query = '''SELECT b.id_berita,b.id_kategori,b.username,b.judul,b.judul_seo,b.headline,b.isi_berita,b.gambar,b.nama_lengkap,b.publish,b.hari,DATE_FORMAT(b.tanggal,'%%Y-%%m-%%d') AS tanggal,DATE_FORMAT(b.jam,'%%H:%%m:%%s') AS jam,b.dibaca,b.tag FROM berita b ORDER BY b.dibaca DESC LIMIT 5'''
        logger.info(query)
        try:
            return self.SelectAll(query)
        except Exception as e:
            raise e