import pandas as pd
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

# 设置 ChromeDriver 路径
chromedriver_path = "./chromedriver.exe"

# 创建 ChromeOptions 对象
chrome_options = Options()

# 创建 ChromeDriver 服务对象
chrome_service = ChromeService(executable_path=chromedriver_path)

# 初始化 WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 打开目标网站
driver.get("https://www.104.com.tw/jobs/index/")
# 初始化WebDriver
driver = webdriver.Chrome()

driver.find_element(By.LINK_TEXT, '登入').click()
# time.sleep(6)
# elementi= driver.find_element(By.CLASS_NAME, 'APP-editor-iframe')
# driver.switch_to.frame(elementi) 
# iframe = driver.find_element(By.TAG_NAME, 'iframe')
# driver.switch_to.frame(iframe)


email = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

email.send_keys('H225541548')
password.send_keys('julia5492065')

time.sleep(10)
# 使用 time.sleep() 保持脚本运行一段时间
print("The browser will remain open for 60 seconds.")

# # 定位帳號欄位
# email = driver.find_element(By.ID, "email")
 
# # 定位密碼欄位
# password = driver.find_element(By.ID, "pass")

# def getData(url):
#     #建立一個Request物件，附加Request Headers的資訊
#     request=req.Request(url, headers={
#         "cookie": "over18=1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
#     })
#     with req.urlopen(request) as response:
#         data=response.read().decode("utf-8")
#     # print(data)

#     #解析原始碼，取得每天文章的標題
#     import bs4
#     root=bs4.BeautifulSoup(data, "html.parser")#讓Beautifulsoup 協助解析HTML格式文件
#     titles=root.find_all("div", class_="title")#尋找 class="title"的div標籤
#     for title in titles:
#         if title.a!=None:
#             print(title.a.string)
#     #抓取上一頁連結
#     nextLink=root.find("a", string="‹ 上頁")
#     return nextLink["href"]

# #主程序:抓取一個頁面的標題
# pageURL="https://pda.104.com.tw/work/jobStore"
# count=0
# while count<5:
#     pageURL="https://www.ptt.cc"+getData(pageURL)
#     # print(pageURL)
#     count+=1