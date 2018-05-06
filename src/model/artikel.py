'''
Created on May 6, 2018

@author: nopri
'''

from marshmallow import Schema, fields, post_load

class Artikel():
    def __init__(self,id,username,judul,seo,isi,gambar,publish,hari,tanggal,jam,dibaca,tag_seo,buletin):
        self.id = id
        self.username = username
        self.seo = seo
        self.isi = isi
        self.gambar = gambar
        self.publish = publish
        self.hari = hari
        self.tanggal = tanggal
        self.jam = jam
        self.dibaca = dibaca
        self.tag_seo = tag_seo
        self.buletin = buletin
        
    def __repr__(self):
        return '<Artikel(name={self.id!r})>'.format(self=self)
    
class ArtikelSchema(Schema):
    id = fields.Str
    username = fields.Str
    seo = fields.Str
    isi = fields.Str
    gambar = fields.Str
    publish = fields.Str
    hari = fields.Str
    tanggal = fields.Date
    jam = fields.Str
    dibaca = fields.Int
    tag_seo = fields.Str
    buletin = fields.Str
    
    @post_load
    def make_Artikel(self,data):
        return Artikel(**data)
        