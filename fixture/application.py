from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.open_home_page()


    def open_home_page(self):
        base_url = 'https://calamian-sqa.syapse.com'
        self.driver.get(base_url)


    def destroy(self):
        self.driver.quit()
        # pass

