import unittest
from selenium import webdriver
from Pages.stock_page import StockPages


class TestStockPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_drop_down_menu(self):
        home_page = StockPages(self.driver)
        home_page.move_trading_information()
        home_page.select_data()
        home_page.daily_closing_price_td()
        home_page.daily_closing_price_screenshot()

    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
