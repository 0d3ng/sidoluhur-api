'''
Created on May 8, 2018

@author: nopri
'''
from flask_restful import Resource,request
from dao.ArtikelDao import ArtikelDao
from flask_jsonpify import jsonify
from util.Message import Message
import logging

logger = logging.getLogger(__name__)

class Artikel(Resource):
    def get(self):        
        message = Message()
        setattr(message, 'link', request.url)
        try:
            setattr(message, 'message', "Success")
            artikelDao = ArtikelDao()
            result = artikelDao.GetAllArtikel()
            if result is None:
                setattr(message,'code',404)           
                setattr(message, 'developerMessage', "Data is empty")
                setattr(message, 'data', None)
            else:            
                setattr(message,'code',200)
                setattr(message, 'developerMessage', None)
                setattr(message, 'data', result)
            logger.info(message.GetResponse())
        except Exception as e:
            logger.error(e)
            setattr(message,'code',500)
            setattr(message, 'message', "Fail")
            setattr(message, 'developerMessage', str(e))
            setattr(message, 'data', None)
        res = message.GetResponse()
        return jsonify(res)