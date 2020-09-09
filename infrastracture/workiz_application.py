from infrastracture import test_configuration
from Pages import landing_page
from Pages import main_page


class WorkizApplication:

    def __init__(self, driver, with_login=True):
        self.landing_page = landing_page.LandingPage(driver)
        if with_login:
            self.main_page = self.login(test_configuration.email, test_configuration.password)
        else:
            self.main_page = main_page.Main_page(self.driver)

    def login(self, email, password):
        return self.landing_page.login(email, password)

    def create_job_from_plus_button(self):
        job_page = self.main_page.add_job_from_click_plus()
        job_page.fill_defualt_values()
        job_page.submit()





