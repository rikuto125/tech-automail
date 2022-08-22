from bs4 import BeautifulSoup
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    url = "https://tech-guild.jp/contact-lp/"
    # webdriverを最新にする
    webdriver = webdriver.Chrome(ChromeDriverManager().install())
    webdriver.get(url)

    # htmlを取得する
    html = webdriver.page_source

    # htmlから要素を抽出する
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    time.sleep(3)

    # ページをActionChainsを使用して13秒かけて下にスクロールする
    actions = ActionChains(webdriver)

    # page downを押しながら13秒かけてスクロールする
    i = 0
    while i < 19:
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        time.sleep(1)
        i += 1

    # actions.send_keys(Keys.END)
    actions.perform()
    # time.sleep(13)

    # webdriver.execute_script("window.scrollBy(0,16500)")

    time.sleep(3)

    # Name
    elem = webdriver.find_element(By.XPATH, '//*[@id="wpforms-87-field_0"]')
    elem.clear()
    time.sleep(1)
    elem.send_keys("Demo")

    # Email
    elem = webdriver.find_element(By.XPATH, '//*[@id="wpforms-87-field_1"]')
    elem.clear()
    time.sleep(1)
    elem.send_keys("flyawerat@na-cat.com")

    # 電話番号
    elem = webdriver.find_element(By.XPATH, '// *[ @ id = "wpforms-87-field_3"]')
    elem.clear()
    time.sleep(1)
    elem.send_keys("11122223333")

    # 下に下げる
    actions.send_keys(Keys.PAGE_DOWN)
    actions.perform()
    time.sleep(1)

    # フリーランスをクリックする
    elem = webdriver.find_element(By.XPATH, '//*[@id="wpforms-87-field_4"]/li[2]/label')
    elem.click()
    time.sleep(1)

    # スキルアップクリックする
    elem = webdriver.find_element(By.XPATH, '//*[@id="wpforms-87-field_5"]/li[3]/label')
    elem.click()
    time.sleep(1)

    # ページを16500ピクセル下にスクロールする
    webdriver.execute_script("window.scrollBy(0,17500)")

    # 経験なしクリック
    elem = webdriver.find_element(By.XPATH, '// *[ @ id = "wpforms-87-field_6"] / li[1]')
    elem.click()
    time.sleep(1)

    # 予約
    elem = webdriver.find_element(By.XPATH, '// *[ @ id = "wpforms-87-field_11"]')
    elem.clear()
    time.sleep(1)
    elem.send_keys("１月１１日１８：００ １月１４日１９：００　　")

    # submit
    elem = webdriver.find_element(By.XPATH, '// *[ @ id = "wpforms-submit-87"]')
    time.sleep(1)
    elem.click()

    # webdriver終了
    time.sleep(10)
    webdriver.quit()


