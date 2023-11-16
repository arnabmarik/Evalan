
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1?crid=MD6BB5RJRZ37&keywords=instant%2Bpot%2Bduo&qid=1699197861&sprefix=instant%2Bpot%2Bdu%2Caps%2C175&sr=8-1&th=1")
#
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#
# print(f" the price is {price_dollar}.{price_cents}")


# finding element by name, id and css selector

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)# it gives us that this is an input tag
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print( documentation_link.text)


# # find element by X-Path
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver.get("https://www.python.org/")
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.close()
# driver.quit()