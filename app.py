from flask import Flask, request, jsonify, render_template
from scraper import scrape_events
from excel_store import update_excel

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fetch-events")
def fetch_events():
    try:
        city = request.args.get("city", "mumbai")
        events = scrape_events(city)

        update_excel(events)

        return jsonify({
            "status": "success",
            "city": city,
            "events_processed": len(events)
        })
    except Exception as e:
        print("BACKEND ERROR:", e)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
