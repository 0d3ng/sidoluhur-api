'''
Created on May 12, 2018

@author: nopri
'''

from flask_restful import Resource,request
from flask_jsonpify import jsonify
import logging
from util.Message import Message
from builtins import setattr
from dao.PageDao import PageDao

logger = logging.getLogger(__name__)

class Page(Resource):
    def get(self):
        message = Message()
        setattr(message, 'link', request.url)
        try:
            setattr(message, 'message', "Success")
            pageDao = PageDao()
            result = pageDao.GetAllPages()
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