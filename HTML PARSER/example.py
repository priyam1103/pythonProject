import requests
from bs4 import BeautifulSoup

result=requests.get("https://www.whitehouse.gov/briefings-statements/")

src=result.content
soup=BeautifulSoup(src,'html')
urls=[]
posts=[]

print("Current headlines from white house")
print("---------------------------------")

for h2_tag in soup.find_all("h2"):
    a_tag=h2_tag.find('a')
    print(a_tag.text)
print("Current headlines from white house realted to TRUMP")
print("---------------------------------")
for h2_tag in soup.find_all("h2"):
    a_tag=h2_tag.find('a')
    if "Trump" in a_tag.text:
          print(a_tag.text)
print("Current headlines timing")
print("---------------------------------")

for articles in soup.find_all("time"):
        print(articles.text)

