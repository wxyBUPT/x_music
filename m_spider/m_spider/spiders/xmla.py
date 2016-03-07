# -*- coding: utf-8 -*-
from __future__ import absolute_import
import urlparse

import scrapy

from music.models import XMLYdpMeta,XMLYAlbum,XMLYSounds

from ..items import XMLYAlbumItem,XMLYSoundsItem

def get_start_urls():
    '''
    通过Django数据库获得开始爬取的url
    :return:
    '''
    xmlydpMetas = XMLYdpMeta.objects.all()
    for xmlydpMeta in xmlydpMetas:
        page_count = xmlydpMeta.end_page
        for i in range(1,page_count+1):
            url = urlparse.urljoin(xmlydpMeta.base_url,str(i))
            #print url
            yield url


class XmlaSpider(scrapy.Spider):
    name = "xmla"
    allowed_domains = ["ximalaya.com"]

    start_urls = get_start_urls()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,self.parse
            )

    #下面的操作负责获得专辑相关的信息，包括专辑相关的url，专辑的名称
    def get_music_item(self,response):
        '''
        获得所有的item
        :param response:
        :return:
        '''
        typeInfo = response.xpath(
            '/html/body/div[3]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]'
        )
        typeUrl = typeInfo.xpath(
            'a/@href'
        ).extract()[0]
        typeName = typeInfo.xpath(
            'a/text()'
        ).extract()[0]
        author = response.css(
            'div.username'
        ).xpath('text()').extract()[0].strip()
        print author
        print u'子啊这里保存专辑信息'
        sounds = response.xpath(
            '/html/body/div[3]/div/div/div[1]/div/div[2]/div[4]/ul/li'
        )
        for sound in sounds:
            info = sound.xpath('div/a[2]')
            title = info.xpath('@title').extract()[0].strip()
            url = info.xpath('@href').extract()[0].strip()
            print title
            print url
        print u'需要在这里保存声音的相关信息'

    def parse(self, response):
        '''
        使用
        :param response:
        :return:
        '''
        xmlyAlbumItem = XMLYAlbumItem()
        tags = response.xpath(
            '/html/body/div[3]/div/div/div[4]/div[1]/div'
        )
        for tag in tags:
            url = tag.xpath('a/@href').extract()[0]
            yield scrapy.Request(
                url,self.get_music_item
            )