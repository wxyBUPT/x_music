#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AllFm(models.Model):
    '''
    所有需要爬取的fm
    '''
    fm_name = models.CharField(max_length=20)
    url = models.URLField()


# 定义爬取喜马拉雅fm 的爬取元数据（包括爬取网站内容）
# 以下模型与喜马拉雅实现逻辑相关，
# 不同网站的业务逻辑实现不同，例如喜马拉雅和考拉虽然网站结构类似，但是爬取逻辑也不同
# 当前时间为  datetime.datetime(2016, 3, 4, 11, 14, 22, 322680)
# 喜马拉雅fm网站形式如果改变需要重新维护本模型相关的代码
class XMLYdpMeta(models.Model):
    '''
    次模型为喜马拉雅fm 发现 -> 节目分类 -> 类别
    '''
    #对应页面的 热门 有声书 综艺娱乐等内容
    #即为类别名称
    tag = models.CharField(max_length=10,verbose_name=u'节目类别')
    base_url = models.URLField(verbose_name=u'节目列表url')
    end_page = models.IntegerField(
        verbose_name=u'节目列表最大索引',help_text=u'帮助scrapy了解所有有效的url'
    )

class XMLYAlbum(models.Model):
    '''
    本数据为通过爬虫获得。
    喜马拉雅fm 发现 -> 节目分类 -> 对应分类 -> 每一个专辑
    '''
    xmlydpMeta = models.ForeignKey(
        XMLYdpMeta
    )
    url = models.URLField()
    name = models.CharField(max_length=50)
    play_times = models.IntegerField(default=0,null=True,blank=True)
    author = models.CharField(max_length=20,null=True,blank=True)

class XMLYSounds(models.Model):
    '''
    本类数据为通过爬虫获得
    数据内容为每一个专辑下面对应的声音
    '''
    xmlyAlbum = models.ForeignKey(
        XMLYAlbum
    )
    name = models.CharField(max_length=50)
    url = models.URLField()