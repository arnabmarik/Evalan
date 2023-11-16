
from  bs4 import BeautifulSoup
import lxml

#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser") #in some cases need to use lxml parser
#
# print(soup.title.string)
#
# # print(soup.prettify())
# print(soup.a) #gives the first anchor tag
# print(soup.li)#gives the first anchor tag
#
# print(soup.find_all(name="a"))
# print(soup.find_all(name="p"))
#
# print([tag.getText() for tag in soup.find_all(name="a")])
# print([tag.get("href") for tag in soup.find_all(name="a")])
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# print(soup.find(name="h3", class_="heading"))
#
# # drill down and select something specifc based on html selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)


import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)

# print([tag.getText() for tag in soup.find_all(name="span a", class_="titleline")])
article_text = [tag.getText() for tag in soup.find_all(name="span", class_="titleline")]
article_links = [tag.get("href") for tag in soup.find_all('a', rel="noreferrer")]
article_upvote = [int(tag.getText().split(" ")[0]) for tag in soup.find_all(name="span", class_="score")]
sorted_upvote = sorted(article_upvote)


print(article_upvote)
print(article_text)
print([(article_text[article_upvote.index(i)], i) for i in sorted_upvote])

