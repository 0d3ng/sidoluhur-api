'''
Created on May 12, 2018

@author: nopri
'''

from flask_restful import Resource,request
from flask_jsonpify import jsonify
import logging
from util.Message import Message
from builtins import setattr
from dao.BeritaDao import BeritaDao

logger = logging.getLogger(__name__)

class Berita(Resource):
    
    def get(self):
        message = Message()
        setattr(message, 'link', request.url)
        try:
            setattr(message, 'message', "Success") 
            beritaDao = BeritaDao()
            result = None
            if 'id_berita' in request.args:
                id_berita = int(request.args['id_berita'])
                logger.info(id_berita)
                result = beritaDao.GetBeritaById(id_berita)
                logger.info(result)
            elif 'limit' in request.args:
                limit = int(request.args['limit'])
                logger.info(limit)
                result = beritaDao.GetBeritaLimit(limit)
            else:          
                result = beritaDao.GetAllBerita()
            if result is None:
                setattr(message,'code',404)           
                setattr(message, 'developerMessage', "Data not found")
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

class BeritaPopular(Resource):
    def get(self):
        message = Message()
        setattr(message, 'link', request.url)
        try:
            setattr(message, 'message', "Success") 
            beritaDao = BeritaDao()     
            result = beritaDao.GetBeritaPopular()
            if result is None:
                setattr(message,'code',404)           
                setattr(message, 'developerMessage', "Data not found")
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