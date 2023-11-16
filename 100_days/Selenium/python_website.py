from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.python.org/")

# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time
time_list = [i.text for i in driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")]
events_list = [i.text for i in driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")]

print(time_list)
print(events_list)

dict = {i:{'time': time_list[i], 'name': events_list[i]} for i in range(len(time_list))}
print(dict)

driver.close()
driver.quit()