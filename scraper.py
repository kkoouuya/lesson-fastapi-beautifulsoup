import requests
import bs4


class Scraper():
  def google_search(self, keyword):
    search_url = "https://www.google.com/search?q="+keyword
    search_response = requests.get(search_url)
    
    soup = bs4.BeautifulSoup(search_response.text, 'lxml')
    parsed_page = soup.select('div.kCrYT>a')
    
    items = []
    rank = 1
    for site in parsed_page:
      item = {
        "rank": rank,
        "title": site.select('h3.zBAuLc')[0].text,
        "url": site.get('href').split('&sa=U&')[0].replace('/url?Q=', '')
      }
      rank += 1
      items.append(item)
    return items