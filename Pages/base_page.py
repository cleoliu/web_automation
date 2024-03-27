import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
        self.set_window_size((1440, 768))
        self.timeout = 20

    def set_window_size(self, window_size: tuple):
        """設定 window size

        Args:
            window_size (tuple): window size
        """
        self.driver.set_window_size(window_size[0], window_size[1])

    def get_page(self, url: str):
        """打開頁面

        Args:
            url (str): url
        """
        self.driver.get(url)

    def find_element(self, locator: tuple):
        """隱式等待找到元素

        Args:
            locator (tuple): locator

        Returns:
            _type_: element
        """
        return WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_element_located(locator)
        )

    def move(self, locator: tuple):
        """滑鼠移動至元素

        Args:
            locator (tuple): locator
        """
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        
    def click(self, locator: tuple):
        """點擊元件

        Args:
            locator (tuple): locator
        """
        self.find_element(locator).click()

    def enter_text(self, locator: tuple, text: str):
        """輸入文字

        Args:
            locator (tuple): locator
            text (str): text
        """
        self.find_element(locator).send_keys(text)

    def select_by_value(self, locator: tuple, value):
        """下拉選單 by value

        Args:
            locator (tuple): locator
            value (_type_): value
        """
        Select(self.find_element(locator)).select_by_value(value)


    def get_screenshot_as_file(self, filename: str):
        """截圖

        Args:
            filename (str): filename
        """
        self.driver.get_screenshot_as_file(filename)

    def scroll_into_view(self, locator: tuple):
        """滾動到出現指定元素

        Args:
            locator (tuple): locator
        """
        eles = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", eles)
        time.sleep(5)

    def get_td_text(self, locator: tuple) -> list:
        """取得 table 裡 td 的 text 內容

        Args:
            locator (tuple): locator

        Returns:
            list: table 裡 td 的 text 內容
        """
        table_element = self.find_element(locator)
        td_elements = table_element.find_elements(By.TAG_NAME, "td")

        return [td_element.text for td_element in td_elements]
