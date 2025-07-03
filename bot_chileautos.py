import os, time, threading
from bs4 import BeautifulSoup
import requests
from telegram import Bot
from flask import Flask

# Configuración desde variables de entorno
TOKEN = os.getenv("TOKEN")
CHAT = os.getenv("CHAT")
url = "https://www.chileautos.cl/auto/particulares/"
TIEMPO = 600  # 10 minutos

bot = Bot(token=TOKEN)
seen = set()

def revisar():
    while True:
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            for auto in soup.select(".result-item"):
                titulo = auto.select_one(".title").get_text(strip=True)
                link = auto.select_one("a.result-link")["href"]
                if link not in seen:
                    seen.add(link)
                    bot.send_message(chat_id=CHAT, text=f"{titulo}\n🔗 https://www.chileautos.cl{link}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(TIEMPO)

# Hilo del bot
threading.Thread(target=revisar, daemon=True).start()

# Servidor web falso para Render (necesario para evitar error de puerto)
app = Flask(__name__)
@app.route("/")
def home():
    return "Bot Chileautos funcionando"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
