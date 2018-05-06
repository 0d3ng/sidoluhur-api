'''
Created on May 6, 2018

@author: nopri
'''

from marshmallow import Schema, fields, post_load

class Agenda():
    def __init__(self,id,username,tema,tema_seo,isi,tempat,pengirim,tgl_mulai,tgl_selesai,tgl_posting,jam,gambar):
        self.id = id
        self.username = username
        self.tema = tema
        self.tema_seo = tema_seo
        self.isi = isi
        self.tempat = tempat
        self.pengirim = pengirim
        self.tgl_mulai = tgl_mulai
        self.tgl_selesai = tgl_selesai
        self.tgl_posting = tgl_posting
        self.jam = jam
        self.gambar = gambar
        
    def __repr__(self):
        return '<Agenda(name={self.id!r})>'.format(self=self)
    
class AgendaSchema(Schema):
    id = fields.Number
    username = fields.Str
    tema = fields.Str
    tema_seo = fields.Str
    isi = fields.Str
    tempat =fields.Str
    pengirim = fields.Str
    tgl_mulai = fields.Date
    tgl_selesai = fields.Date
    tgl_posting = fields.Date
    jam = fields.Str
    gambar = fields.Str
    
    @post_load
    def make_agenda(self,data):
        return Agenda(**data)
    