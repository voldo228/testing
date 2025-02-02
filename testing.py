from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, json

with open('config.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Сценарий 1
def scen_1():
    try:
        driver = webdriver.Chrome()
        start_time = time.time()  

        driver.get(data['url'])
        driver.maximize_window()
        time.sleep(1)
        
        btn = driver.find_element(By.XPATH, data['xpath_1'])
        btn.click()
        time.sleep(1)

        btn2 = driver.find_element(By.XPATH, data['xpath_2'])
        btn2.click()
        time.sleep(1)

    finally:
        end_time = time.time()  
        execution_time = end_time - start_time
        driver.quit()
        return execution_time


# Сценарий 2
def scen_2():
    try:
        driver = webdriver.Chrome()
        start_time = time.time()  

        driver.get(data['url'])
        driver.maximize_window()
        time.sleep(1)
        

        btn = driver.find_element(By.XPATH, data['xpath_1'])
        btn.click()
        time.sleep(1)

        search_box = driver.find_element(By.NAME, "search")


        search_query = "мегаладония"  
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)  


        first_article = driver.find_element(By.CSS_SELECTOR, "body > div.screen_one > div.row > button") 
        first_article.click()
        time.sleep(1)

    finally:
        end_time = time.time()  
        execution_time = end_time - start_time
        driver.quit()
        return execution_time

if __name__ == '__main__':
    print(f"Время выполнения сценария 1, вариант 1: {scen_1():.2f} секунд")
    print(f"Время выполнения сценария 1, вариант 2: {scen_2():.2f} секунд")