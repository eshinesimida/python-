# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:22:32 2019

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid

import random
import csv
import os

driver = webdriver.Chrome()
username = "454656783@qq.com"#登录账户名
password = "lxb454656783"#password
url = 'http://glidedsky.com/level/web/crawler-basic-1'
print(url)
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(80)
time.sleep(4)
response = HtmlResponse(url="my HTML string", body=driver.page_source, encoding="utf-8")
#company = response.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[1]/span[1]/text()').extract()
#print(company)

time.sleep(3)
#//*[@id="email"]//*[@id="password"]//*[@id="app"]/main/div/div/div/div/div[2]/form/div[4]/div/button
elem = driver.find_element_by_xpath(
        '//*[@id="email"]');

elem.send_keys(username)
elem = driver.find_element_by_xpath(
        '//*[@id="password"]');
elem.send_keys(password)

driver.find_element_by_xpath(
        '//*[@id="app"]/main/div/div/div/div/div[2]/form/div[4]/div/button').click()
time.sleep(random.uniform(3, 6))

response = HtmlResponse(url="my HTML string", body=driver.page_source, encoding="utf-8")



B = response.xpath('//div[@class="row"]/div')
numbers = []
for a in B:
    number = a.xpath('text()').extract()[0]
    number = number.strip()
    numbers.append(int(number))
    print(number)
    
sum(numbers)


###########################################
#第二题

url = 'http://glidedsky.com/level/web/crawler-basic-2?page=1'
urls = []
for i in range(1000):
    url = 'http://glidedsky.com/level/web/crawler-basic-2?page=' + str(i+1)
    urls.append(url)
numbers = []  
urls1 = urls[974:]  
for url in urls1:
    print(url)
    time.sleep(1)
    driver.get(url)
    response = HtmlResponse(url="my HTML string", body=driver.page_source, encoding="utf-8")
    B = response.xpath('//div[@class="row"]/div')
    
    for a in B:
        number = a.xpath('text()').extract()[0]
        number = number.strip()
        numbers.append(int(number))

