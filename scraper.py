import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0"}

def executar():
    url = "https://example.com"

    html = requests.get(url, headers=HEADERS, timeout=15).text
    soup = BeautifulSoup(html, "lxml")

    titulo = soup.find("h1").text.strip()

    df = pd.DataFrame([{
        "titulo": titulo,
        "coletado_em": datetime.now().isoformat()
    }])

    df.to_csv("teste.csv", index=False)

    print("Scraping teste executado com sucesso.")
