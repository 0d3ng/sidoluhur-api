'''
Created on May 10, 2018

@author: nopri
'''

class Message():
    '''
    Template response
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.code = 0
        self.message = None
        self.link = None
        self.developerMessage = None
        self.data = None
        
    def GetResponse(self):
        response = {
                    'code':self.code,
                    'message':self.message,
                    'link':self.link,
                    'developerMessage':self.developerMessage,
                    'data':self.data
        }
        return response