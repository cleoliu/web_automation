from Utils.locators import HomePage, DailyClosingPricePage
from Pages.base_page import BasePage
import time


class StockPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.get_page("https://www.twse.com.tw/zh/index.html")

    def move_trading_information(self):
        self.move(HomePage.trading_information)
        self.move(HomePage.daily_closing_price)
        self.click(HomePage.daily_closing_price)
        
    def select_data(self):
        self.select_by_value(DailyClosingPricePage.select_y, "2023")
        self.select_by_value(DailyClosingPricePage.select_m, "1")
        self.enter_text(DailyClosingPricePage.stock_no, "2330")
        self.click(DailyClosingPricePage.search)
        
    def daily_closing_price_td(self):
        tds = self.get_td_text(DailyClosingPricePage.table)
        print("daily_closing_price:", tds[1::2])
        
    def daily_closing_price_screenshot(self):
        self.scroll_into_view(DailyClosingPricePage.average_monthly)
        self.get_screenshot_as_file(f"screenshot_{time.time()}.png")

