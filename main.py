from fastapi import FastAPI, HTTPException
from scraper import Scraper


app = FastAPI()
scraper = Scraper()


@app.get("/{word}")
async def search_google(word):
  items = scraper.google_search(word)
  if len(items) == 0:
    raise HTTPException(status_code=404, detail="Not found")
  return items