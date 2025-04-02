import requests
import bs4


page_still_valid = True
authors = set()
url = 'https://quotes.toscrape.com/page/'
page = 1
while page_still_valid:
    page_url = url+ str(page)
    result = requests.get(page_url)
    if "No quotes found!" in result.text:
        break

    soup = bs4.BeautifulSoup(result.text ,"lxml")
    for name in soup.select(".author"):
        authors.add(name.text)

    page += 1

print(authors)