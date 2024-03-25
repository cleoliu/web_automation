import unittest
from selenium import webdriver
from Pages.trade_page import TradePages


class TestTradePages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_drop_down_menu(self):
        home_page = TradePages(self.driver)
        home_page.trading_information()
        home_page.select_date()
        home_page.daily_closing_price()
        home_page.screenshot()

    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
