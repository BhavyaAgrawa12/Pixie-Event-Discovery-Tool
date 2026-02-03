# Pixie Event Discovery Tool

A full-stack web application built as part of the **Pixie Internship Assignment** to discover, fetch, and store public event data for selected cities.

The project demonstrates an end-to-end workflow covering **web scraping**, **backend API design**, **data persistence**, and a **simple frontend interface**.

---

## 🚀 Features

- Fetches **real public events** from **AllEvents.in**
- City-based event discovery
- Pagination support to fetch multiple events
- Deduplication using unique event IDs
- Persistent local storage using **Excel**
- Simple web UI to trigger and monitor data fetching
- Clean separation of frontend, backend, scraping, and storage logic

---

## 🛠️ Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript (Fetch API)

### Backend
- Python  
- Flask

### Web Scraping
- `requests`  
- `BeautifulSoup`

### Storage
- Local Excel file (`events.xlsx`)  
- `pandas` + `openpyxl`

---

## 📂 Project Structure

```
Pixie-Event-Discovery-Tool/
├── app.py                # Flask application (routes & orchestration)
├── scraper.py            # Event scraping logic (AllEvents.in)
├── excel_store.py        # Excel storage & deduplication logic
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   ├── style.css         # Styling
│   └── app.js            # Frontend JavaScript
├── README.md
└── .gitignore
```

> ⚠️ `events.xlsx` is generated automatically at runtime and is **not committed** to the repository.

---

## ⚙️ How the Application Works

1. User selects a city from the web interface  
2. Frontend sends a request to `/fetch-events`  
3. Backend:
   - Scrapes event data from **AllEvents.in**
   - Handles pagination to fetch multiple pages
   - Removes duplicate events
4. Events are stored or updated in a local Excel file
5. UI displays the total number of events fetched

---

## 🧪 Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/BhavyaAgrawal12/Pixie-Event-Discovery-Tool.git
cd Pixie-Event-Discovery-Tool
```

### 2️⃣ Install dependencies
```bash
pip install flask requests beautifulsoup4 pandas openpyxl
```

### 3️⃣ Run the application
```bash
python app.py
```

### 4️⃣ Open in browser
```
http://127.0.0.1:5000
```

---

## 📊 Data Storage

- Event data is stored locally in **`events.xlsx`**
- The file is **auto-created** on the first fetch
- The same file is reused and updated on every run
- Duplicate events are avoided automatically

### Excel Schema

```
event_id | event_name | event_date | venue | city | category | link | status | last_updated | source
```

---

## 🔐 Deduplication Strategy

- Each event is assigned a unique `event_id`
- Generated using a hash of:
  - Event name
  - Event date
  - Venue
- If an event already exists, its row is updated instead of duplicated

---

## 🌐 Data Source

- **AllEvents.in**  
  A public event aggregation platform that exposes server-rendered event listings.

> Due to platform limitations, some event attributes (such as exact dates or venues) are standardized or inferred.

---

## ⚠️ Limitations

- Scraping depends on publicly available HTML
- JavaScript-heavy platforms are not used
- Changes in website structure may affect scraping results

---

## ✅ Why Local Excel Storage?

- No external credentials or APIs required
- Easy to inspect and verify data
- Simple, reproducible setup
- Suitable for local development and demos

The storage layer is designed so it can be replaced with a database or cloud service if needed.

---

## 🧠 Key Concepts Demonstrated

- Full-stack application flow
- Web scraping fundamentals
- Backend API design
- Persistent data storage
- Deduplication logic
- Clean separation of concerns

---

## 📌 Future Enhancements

- Improve event metadata extraction
- Add filters (date, category)
- Replace Excel with a database
- Deploy backend to cloud hosting

---

## 👤 Author

**Bhavya Agrawal**  
Built as part of the **Pixie Internship Assignment**

---

### ✅ Status
**Project complete and submission-ready.**
