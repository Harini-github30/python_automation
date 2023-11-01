from selenium import webdriver
import time


def get_driver():
#set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start_maximized") # maximized version ofthe browser
    options.add_argument("disable-dev-shm-usage")  #to avoid issues in linux
    options.add_argument("no-sandbox") 
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled") #enables detection from browser


    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def get_temp(text):
    temp = float(text.split(": ")[1])
    print("The average temperature is: ",temp)
    return temp

def main():
    driver = get_driver()
    time.sleep(2) #makes the browser hold on


    ##scrape static value
    # element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]") # can also use by="xpath" without importing
    # return element

    ##scrape dynamic value
    element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]") # can also use by="xpath" without importing
    return get_temp(element.text)


print(main())
