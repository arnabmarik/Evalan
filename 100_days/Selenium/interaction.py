
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# article_count = driver.find_element(By.ID, value="articlecount").find_element(By.TAG_NAME, "a")
# print(article_count.text)


article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

article_count.click()





driver.close()
driver.quit()