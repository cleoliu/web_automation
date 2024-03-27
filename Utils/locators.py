from selenium.webdriver.common.by import By


class HomePage:
    trading_information = (By.XPATH, "/html/body/div[1]/header/nav/ul/li[2]/a")
    daily_closing_price = (
        By.XPATH,
        "/html/body/div[1]/header/nav/ul/li[2]/div/div/ul[1]/li[10]/a",
    )


class DailyClosingPricePage:
    select_y = (By.NAME, "yy")
    select_m = (By.NAME, "mm")
    stock_no = (By.NAME, "stockNo")
    search = (
        By.XPATH,
        "/html/body/div[1]/div/div[2]/main/form/div/div[1]/div[3]/button",
    )
    table = (By.TAG_NAME, "table")
    average_monthly = (By.XPATH, "/html/body/div[1]/div/div[2]/main/div[2]/hgroup/h2")
