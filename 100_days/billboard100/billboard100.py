from bs4 import *

import requests
print("which year do you want to travel to?")
response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-08-12")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)

article_text = [tag.getText() for tag in soup.find_all(name="h3", id="title-of-a-story", class_="c-title")]
print(article_text)