from Utils.locators import HomePageLocators, DailyClosingPrice
from Pages.base_page import BasePage
import time


class TestTrade(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.get_page("https://www.twse.com.tw/zh/index.html")


    def trading_information(self):
        self.move(HomePageLocators.trading_information)
        self.move(HomePageLocators.daily_closing_price)
        self.click(HomePageLocators.daily_closing_price)
        
    def select_date(self):
        self.select_by_value(DailyClosingPrice.select_y, "2023")
        self.select_by_value(DailyClosingPrice.select_m, "1")
        self.enter_text(DailyClosingPrice.stock_no, "2330")
        self.click(DailyClosingPrice.search)
        
    def daily_closing_price(self):
        tds = self.get_td(DailyClosingPrice.table)
        print("daily_closing_price:", tds[1::2])
        
    def screenshot(self):
        self.scroll_into_view(DailyClosingPrice.average_monthly)
        self.get_screenshot_as_file(f"screenshot_{time.time()}.png")

