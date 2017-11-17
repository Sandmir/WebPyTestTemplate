from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='/Applications/Python 3.5/geckodriver')
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)


    def open_home_page(self):
        base_url = ''
        self.driver.get(base_url)


    def destroy(self):
        self.driver.quit()
        # pass

