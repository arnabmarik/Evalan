import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title)


movie_text = [tag.getText() for tag in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
movie_text.reverse()

with open("100_movies.txt", "w") as f:
    [f.write(f'{i}\n') for i in movie_text]



