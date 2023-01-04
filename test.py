# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.common.by import By


# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument('--user-agent=%s' % user_agent)

url = "https://www.ptt.cc/bbs/Keelung/index.html"
# url = "https://www.hermes.com/tw/zh/category/women/bags-and-small-leather-goods/bags-and-clutches"

# 開啟瀏覽器視窗(Chrome)
# driver = webdriver.Chrome()
# res = driver.get(url=url)
# print(res)



driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
#Pagination
pagination = driver.find_element(By.XPATH, '//div[@class="r-ent"]')
title = pagination.find_elements(By.CLASS_NAME, 'title')
print(str(title))
a = pagination.find_elements(By.TAG_NAME, 'a')

print(str(a))
driver.close() # 關閉瀏覽器視窗