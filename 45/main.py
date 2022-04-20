from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/news"

response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(website, 'html.parser')

articles = soup.find_all(name="a", class_="titlelink")
articles_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_points = [int(score.getText().replace("points", "")) for score in soup.find_all(name="span", class_="score")]

index_max_article = article_points.index(max(article_points))

print(
    f"Title: {articles_texts[index_max_article]}\nUpvote: {article_points[index_max_article]}\nLink: {articles_links[index_max_article]}")
