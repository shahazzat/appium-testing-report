from appium import webdriver
import time

import config
import report

##################################################
## This is main test module. User should execute this module to test <project> functionalities.
##################################################
__author__ = "Shahazzat Hossain"
__copyright__ = "Copyright 2021, Project"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Shahazzat Hossain"
__email__ = "shahazzat@gmail.com"
__status__ = "POC"


class Vrit:

    def __init__(self):
        # Invoke driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", config.desired_capabilities)
        self.total_number_of_test = 2
        self.executed_test = 0
        self.failed_test = 0
        self.passed = 0
        self.report = []

    def login_test(self):
        test_report = {"title": "Login test",
                       "type": "Positive",
                       "status": ""
                       }
        self.executed_test += 1
        print(self.driver.current_activity)
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        login_activity_name = self.driver.current_activity
        print(login_activity_name)
        # Email
        #
        email_field = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText')
        email_field.set_value(config.vrit_email)
        password_field = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')
        password_field.set_value(config.vrit_password)

        self.driver.find_element_by_id('com.example.vrit:id/login_btn').click()
        time.sleep(10)
        after_login_activity_name = self.driver.current_activity
        print(after_login_activity_name)
        try:
            assert after_login_activity_name != login_activity_name
        except AssertionError:
            print(config.msg_login_failed)
            self.failed_test += 1
            test_report["status"] = "Failed"

        if test_report["status"] == "":
            self.passed += 1
            test_report["status"] = "Passed"

        self.report.append(test_report)

    def send_message_test(self):
        test_report = {"title": "Send help message",
                       "type": "Positive",
                       "status": ""
                       }
        self.executed_test += 1
        print(self.driver.current_activity)
        self.driver.find_element_by_id('com.example.vrit:id/action_settings').click()

        message_field = self.driver.find_element_by_id('com.example.vrit:id/input_msg_id')
        message_field.set_value(config.msg_so_help)

        self.driver.find_element_by_id('com.example.vrit:id/save_btn').click()
        time.sleep(10)
        display_message_text = self.driver.find_element_by_id('com.example.vrit:id/message_tv').get_attribute('text')

        try:
            assert display_message_text == config.msg_so_help
        except AssertionError:
            print(config.msg_failed_to_send_message)
            self.failed_test += 1
            test_report["status"] = "Failed"

        if test_report["status"] == "":
            self.passed += 1
            test_report["status"] = "Passed"

        self.report.append(test_report)

    def report_summary(self):
        return {
            "total_number_of_test": self.total_number_of_test,
            "passed": self.passed,
            "failed": self.failed_test,
            "not_executed": self.total_number_of_test - (self.passed + self.failed_test)
        }


if __name__ == "__main__":
    vrit = Vrit()
    vrit.login_test()
    # vrit.send_message_test()

    report = report.TestReport()
    report.generate_html(vrit.report, vrit.report_summary())
