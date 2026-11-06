from selenium.webdriver.common.by import By

class OrderFeedLocators:
    HEADER_ORDER_FEED_PAGE = (By.XPATH, "//div[@class='OrderFeed_orderFeed__2RO_j']/h1[text()='Лента заказов']")
    
    COUNTE_OF_ALL_TIME = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']/div[2]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    COUNTE_OF_TODAY = (By.XPATH, "//div[@class='OrderFeed_ordersData__1L6Iv']/div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    FIRST_NUMBER_IN_WORK_SECTION = (By.XPATH, "//div[@class='OrderFeed_orderStatusBox__1d4q2 mb-15']/ul[2][@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[1]")