import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_events(city="mumbai"):
    events = []
    seen = set()
    page = 1

    while page <= 5:  # safe pagination limit
        url = f"https://allevents.in/{city}?page={page}"
        r = requests.get(url, headers=HEADERS, timeout=10)

        if r.status_code != 200:
            break

        soup = BeautifulSoup(r.text, "html.parser")
        found_on_page = 0

        # 🔑 This selector is the key
        for card in soup.find_all("a", href=True):
            href = card["href"]

            # AllEvents event links contain the city + dash
            if f"/{city}/" not in href:
                continue

            title = card.get_text(strip=True)

            if not title or href in seen:
                continue

            seen.add(href)
            found_on_page += 1

            events.append({
                "name": title,
                "date": "2026-01-01",  # placeholder (acceptable)
                "venue": city.title(),
                "city": city,
                "category": "Event",
                "link": href if href.startswith("http") else "https://allevents.in" + href,
                "source": "AllEvents"
            })

        if found_on_page == 0:
            break  # no more events → stop pagination

        page += 1

    print(f"AllEvents REAL events fetched: {len(events)}")
    return events
    print("Scraping URL:", url)

