import time
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.perfil import perfil_browser
import pyperclip

TIMEOUT = '5'


class TestHackaton:
    def __init__(self):
        self.driver = perfil_browser()
        self.list_men = []

    def run(self):
        self.open_site()
        for i in range(280, 630, 70):
            self.call_function(160, i)
        self.driver.close()

        for i in self.list_men:
            print(i)

    def call_function(self, x, y):
        pyautogui.doubleClick(x, y)
        pyautogui.moveTo(517, 603, duration=3)
        pyautogui.click(1017, 603)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        self.list_men.append(pyperclip.paste())

    def open_site(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(10)

    @staticmethod
    def wait_expected_condition(driver, by, locator, ec=EC.presence_of_element_located, timeout=TIMEOUT):
        return WebDriverWait(driver, timeout).until(ec((by, locator)))


if __name__ == '__main__':
    wc = TestHackaton()
    wc.run()
