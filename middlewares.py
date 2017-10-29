# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import time


class JavaScriptMiddleware(object):
    def __init__(self):
        print('is run here--------------------------------------------->>>>')
    @classmethod
    def process_request(self, request, spider):
        #print("PhantomJS is starting...")
        driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe') #指定使用的浏览器
        # driver = webdriver.Firefox()
        driver.get(request.url)
        time.sleep(1)
        # js = "var q=document.documentElement.scrollTop=10000"
        # driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
        time.sleep(3)
        body = driver.page_source.encode('utf-8')
        print(body)
        driver.quit()
        #print ("访问"+request.url)
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
