import time
from appium.webdriver.common.touch_action import TouchAction
from Pages import job_page


class Main_page:

    def __init__(self, driver):
        self.driver = driver

    def add_job_from_click_plus(self):
        self.click_plus()
        return self.choose_job()

    def click_plus(self):
        time.sleep(6)
        TouchAction(self.driver).tap(None, 960, 1486, 1).perform()

    def choose_job(self):
        xpath_job_element = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                            ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup" \
                            "/android.view.ViewGroup[2]/android.view.ViewGroup[1] "
        self.driver.find_element_by_xpath(xpath_job_element).click()
        new_job_page = job_page.Job_page(self.driver)
        return new_job_page