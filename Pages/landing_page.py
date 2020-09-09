from Pages import main_page


class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.choose_login()
        self.insert_email_and_password(email, password)
        self.click_login()
        new_main_page = main_page.Main_page(self.driver)
        return new_main_page

    def choose_login(self):
        xpath_login_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                             ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view" \
                             ".ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout" \
                             "/android.view.ViewGroup[5]/android.widget.TextView "
        self.driver.find_element_by_xpath(xpath_login_button).click()

    def insert_email_and_password(self, email, password):
        xpath_email = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                      "/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[" \
                      "3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view" \
                      ".ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[" \
                      "1]/android.widget.EditText "
        self.driver.find_element_by_xpath(xpath_email).send_keys(email)
        xpath_pass = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                     "/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[" \
                     "3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view" \
                     ".ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[" \
                     "2]/android.widget.EditText "
        self.driver.find_element_by_xpath(xpath_pass).send_keys(password)

    def click_login(self):
        xpath_log_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                           ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view" \
                           ".ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout" \
                           "/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view" \
                           ".ViewGroup[3]/android.widget.TextView "
        self.driver.find_element_by_xpath(xpath_log_button).click()






