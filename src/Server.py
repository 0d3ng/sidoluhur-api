'''
Created on May 6, 2018

@author: nopri
'''

from flask import Flask
from flask_restful import Api
from util.LogUtil import LogUtil
from resources.Agenda import Agenda
from resources.Artikel import Artikel, ArtikelPopular
from resources.Berita import Berita, BeritaPopular
from resources.Category import Category
from resources.Album import Album
from resources.Page import Page
from resources.Galery import Galery

app = Flask(__name__)
api = Api(app)

#Agendas
api.add_resource(Agenda,'/sidoluhur/api/v1.0/agendas')

#Article
api.add_resource(Artikel,'/sidoluhur/api/v1.0/articles')
api.add_resource(ArtikelPopular,'/sidoluhur/api/v1.0/articles/popular')

#News
api.add_resource(Berita,'/sidoluhur/api/v1.0/news')
api.add_resource(BeritaPopular,'/sidoluhur/api/v1.0/news/popular')

#Album
api.add_resource(Album,'/sidoluhur/api/v1.0/albums')

#Category
api.add_resource(Category,'/sidoluhur/api/v1.0/categories')

#Page
api.add_resource(Page,'/sidoluhur/api/v1.0/pages')

#Galery
api.add_resource(Galery,'/sidoluhur/api/v1.0/galeries')

if __name__ == '__main__':
    LogUtil.setup_logging()
    app.run(port=5002,debug=True)