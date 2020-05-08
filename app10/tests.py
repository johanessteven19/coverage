from django.test import TestCase, Client
from django.urls import resolve
from django.http import HttpRequest
# from app.views import index
# from app.models import TopLiked
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest

# Create your tests here.
class Story10Test(TestCase):
    def test_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)
    
    def test_inside_html(self):
        response=Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("Login", response_content)

class FunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')        
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')

        self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(FunctionalTest, self).setUp()

    def test_url_exists(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')

    def test_story10_sign_up_and_check_redirect(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        self.assertIn('You are not logged in!', selenium.page_source)
        signup = selenium.find_element_by_id('signupbutton')
        signup.click()
        selenium.implicitly_wait(10)
        username = selenium.find_element_by_id('id_username')
        username.send_keys("tes2")
        password1 = selenium.find_element_by_id('id_password1')
        password1.send_keys("testestestes")
        password2 = selenium.find_element_by_id('id_password2')
        password2.send_keys("testestestes")
        email = selenium.find_element_by_id('id_email')
        email.send_keys("testes2@gmail.com")
        button = selenium.find_element_by_id('regbutton')
        button.click()
        selenium.implicitly_wait(10)
        self.assertIn('Login!', selenium.page_source)

        
        username = selenium.find_element_by_id('id_username')
        username.send_keys("tes2")
        password = selenium.find_element_by_id('id_password')
        password.send_keys("testestestes")
        button = selenium.find_element_by_id('loginbutton')
        button.click()
        selenium.implicitly_wait(10)
        self.assertIn('Hi tes2!', selenium.page_source)

        logout = selenium.find_element_by_id('logoutbutton')
        logout.click()
        selenium.implicitly_wait(10)
        self.assertIn('You are not logged in!', selenium.page_source)

    def tearDown(self):
        self.selenium.quit()
        super(FunctionalTest, self).tearDown()