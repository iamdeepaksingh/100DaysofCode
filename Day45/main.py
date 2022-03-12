from bs4 import BeautifulSoup
#import lxml

with open("website.html") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.string)
print(soup.prettify())

all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name")
print(name)
print("\n")

headings = soup.select(".heading")
print(headings)