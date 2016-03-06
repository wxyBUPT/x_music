# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from music.models import XMLYAlbum,XMLYSounds


class MSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XMLYAlbumItem(DjangoItem):
    django_model = XMLYAlbum

class XMLYSoundsItem(DjangoItem):
    django_model = XMLYSounds