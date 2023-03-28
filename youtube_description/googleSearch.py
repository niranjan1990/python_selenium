from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
#set chromodriver.exe path
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
#launch URL
driver.get("http://www.google.com")

df = pd.read_csv('CollegeNames.csv')

my_list = []

def getUrls (college):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))
    element.clear()
    element.send_keys(row + ' news')
    #print(row,'row')
    element.send_keys(Keys.ENTER)
    #result = driver.findElement(By.id("rso")).findElements(By.xpath("/*")).get(0).click()
    #result = driver.find_element(By.XPATH, '(//h3)[1]/a').click()
    #result = driver.find_element_by_class_name("iUh30")
    #result = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a').get_attribute('href')
    results = driver.find_elements_by_css_selector('div.g')
    link = results[0].find_element_by_tag_name("a")
    result = link.get_attribute("href")
    #print(result,'result')
    my_list.append(result)
    #df["link"] = result
    #df.to_csv("CollegeNames.csv", index=False)
    #driver.quit()

for index, row in df.iterrows():
    time.sleep(10)
    getUrls(row)

#print(my_list,'mylist')
df['link'] = my_list
df.to_csv("CollegeNames.csv", index=False)

#details_lst = []
#print('df',df)
#for column in df.columns:
    #details_lst.append(df[column][1])
    #print('college',column)
    #element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))
    #element.send_keys(column)
    #element.send_keys(Keys.ENTER)
    #result = driver.find_element_by_class_name("iUh30").text
    #print(result,'result')