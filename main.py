# coding:utf-8
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup



service = Service("/usr/local/bin/chromedriver")

# GoogleChromを起動
driver = webdriver.Chrome(service = service)
driver.implicitly_wait(3)


# ログイン
url_pricone = "https://www.globalnote.jp/login/?redirect_to=https%3A%2F%2Fwww.globalnote.jp/post-12038.html"
driver.get(url_pricone)
driver.implicitly_wait(3)
driver.find_element_by_id('user_login').send_keys('takuowake')
driver.find_element_by_id('user_pass').send_keys('hello')
driver.find_element_by_id('wp-submit').click()
print('ログイン成功')
driver.implicitly_wait(3)
driver.find_element_by_class_name("main_but").click()
# URL先に移動
driver.get("https://www.globalnote.jp/p-data-g/?dno=8170&post_no=12038")
driver.implicitly_wait(5)
# データを表示
driver.find_element_by_id('tab5').click()
driver.find_element_by_xpath('/html/body/div/div/div[3]/table/tbody/tr/td[1]/div/form/div/p[3]/a[1]').click()
driver.find_element_by_class_name("bot").click()


# res = requests.get("https://www.globalnote.jp/p-data-g/?dno=8170&post_no=12038")
# soup = BeautifulSoup(res.text, "html.parser")
# elems = soup.find("a")
# for elem in elems:
#     print(elem.contents[0])
# current_url = browser.current_url
# html = requests.get(current_url)
# bs = BeautifulSoup(html.text, "html.parser")
# fankitPage = bs.find("ul", class_="page-nav").find_all("li")
# page = []

# for li_tag in fankitPage:
#     a_tag = li_tag.find("a")
#     if(a_tag.get('class')):
#         page.append(current_url)
#     else:
#         page.append(a_tag.get("href"))


load_url = "https://www.globalnote.jp/p-data-g/?dno=8170&post_no=12038"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
topic = soup.find(class_="list")
for element in topic.find_all("td"):
   print(element.text)
