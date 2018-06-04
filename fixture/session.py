import time
import allure
from selenium.webdriver.common.keys import Keys

from library.APIGmail import api_get_gmail
from library.lib_selenium import *


def receive_new_psw():
    GMAIL = api_get_gmail()

    user_id = 'me'
    label_id_one = 'INBOX'
    label_id_two = 'UNREAD'

    unread_msgs = GMAIL.users().messages().list(userId=user_id, labelIds=[label_id_one, label_id_two]).execute()

    mssg_list = unread_msgs['messages']
    m_id = mssg_list[0]['id']
    message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()

    snippet = message['snippet']



    new_psw = snippet.split("Your new password to is: ")[1]
    # save new psw

    file_psw = open('/Privite/Study/Python/PyTestSugar/data/password.txt', 'w')
    file_psw.write(new_psw)
    file_psw.close()


class SessionHelper:

    # describe locators here!!!
    greeting_xp = "//img[@alt='Patients']/.."

    def __init__(self, app):
        self.app = app

    def get_new_psw(self):
        # with allure.step('Get valid password'):
        #     file_psw = open('//Privite/Study/Python/PyTestSugar/Data/password.txt', 'r')
        #     new_psw = file_psw.readline()
        #     file_psw.close()
        #     return new_psw
        pass

    def login(self, username = 'testmobile.marina@gmail.com',psw = ''):
        with allure.step('Login step'):
            input = self.app.driver.find_element_by_xpath("//input[@name = 'username']")
            input.send_keys(username)
            time.sleep(3)
            input.send_keys(Keys.ENTER)
            input = self.app.driver.find_element_by_xpath("//input[@name = 'password']")
            input.send_keys(psw)
            time.sleep(3)
            input.send_keys(Keys.ENTER)


    def logout(self):
        with allure.step('Logout step'):
            driver = self.app.driver
            pass

    def forget_psw(self, username=''):
        with allure.step('Forget PSW'):
            driver = self.app.driver
            pass

    def return_to_home_page(self):
        pass

