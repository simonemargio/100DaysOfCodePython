from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
print(soup.find_all(name='li'))
anchor_tag = soup.find_all(name='a')

for single_tag in anchor_tag:
    print(single_tag.get("href"))
    print(single_tag.getText())


print(soup.find(name="h1", id="name"))
print(soup.find(name="h3", class_="heading"))

# an element <p> ... <a> ... <a><p>
url = soup.select(selector="p a")
print(url[1])

url = soup.select_one(selector="p a")
print(url)

# id with css
url = soup.select_one(selector="#name")
print(url)

# class with css
url = soup.select_one(selector=".heading")
print(url)
