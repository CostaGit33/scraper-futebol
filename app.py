from flask import Flask, jsonify
import scraper

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def run_scraper():
    try:
        scraper.executar()
        return jsonify({"status": "ok", "message": "Scraping executado com sucesso"})
    except Exception as e:
        return jsonify({"status": "erro", "message": str(e)}), 500

@app.route("/")
def home():
    return jsonify({"status": "online", "service": "scraper-futebol"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
