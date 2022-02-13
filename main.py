from fastapi import FastAPI
from scraper import Scraper


app = FastAPI()
scraper = Scraper()


@app.get("/{word}")
async def search_google(word: str):
  items = scraper.google_search(word)
  scraper.save_csv(items)
  return items