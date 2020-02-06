from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

import threading

class AbstractDriver:
    
    url_sufix = '' # the first page will have such a suffix
    username = {'username': 'your usename',
                'element_id': 'id_username'}
    
    password = {'password':'your password',
                'element_id': 'id_password'}
    
    button_xpath = '' # inform the Xpath to login button

    def __init__(self, page):
        self.page = page

    def btn_click(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        element.click()

    def type(self, element_id, text):
        element = self.driver.find_element_by_id(element_id)
        element.clear()
        element.send_keys(text)

    def login(self):
        self.type(self.username['element_id'], self.username['username'])
        self.type(self.password['element_id'], self.password['password'])
        self.btn_click(self.button_xpath)

    def start(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.page + self.url_sufix if self.url_sufix else self.page)
    
    def get(self, page):
        self.driver.get(page)
        self.page_source = self.driver.page_source
     
