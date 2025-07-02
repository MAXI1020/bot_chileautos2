import os, requests, time
from bs4 import BeautifulSoup
from telegram import Bot

# Configuración
TOKEN = os.getenv('import os, requests, time
from bs4 import BeautifulSoup
from telegram import Bot

# Configuración
TOKEN = os.getenv('7616697365:AAFvJZ-ZHDIzJt0FFRa1vZkq-LzK3P5gQoM')
CHAT = os.getenv('7927751785')
url = 'https://www.chileautos.cl/auto/particulares/'
TIEMPO = 600  # 10 minutos

bot = Bot(token=TOKEN)
seen = set()

def revisar():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for auto in soup.select('.result-item'):
        titulo = auto.select_one('.title').get_text(strip=True)
        link = auto.select_one('a.result-link')['href']
        if link not in seen:
            seen.add(link)
            texto = f"🚗 *Nuevo auto*: [{titulo}]({link})"
            bot.send_message(chat_id=CHAT, text=texto, parse_mode='Markdown')

if __name__ == '__main__':
    while True:
        try:
            revisar()
        except Exception as e:
            bot.send_message(chat_id=CHAT, text=f"❌ Error: {e}")
        time.sleep(TIEMPO)
')
CHAT = os.getenv('TELEGRAM_CHAT_ID')
url = 'https://www.chileautos.cl/auto/particulares/'
TIEMPO = 600  # 10 minutos

bot = Bot(token=TOKEN)
seen = set()

def revisar():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for auto in soup.select('.result-item'):
        titulo = auto.select_one('.title').get_text(strip=True)
        link = auto.select_one('a.result-link')['href']
        if link not in seen:
            seen.add(link)
            texto = f"🚗 *Nuevo auto*: [{titulo}]({link})"
            bot.send_message(chat_id=CHAT, text=texto, parse_mode='Markdown')

if __name__ == '__main__':
    while True:
        try:
            revisar()
        except Exception as e:
            bot.send_message(chat_id=CHAT, text=f"❌ Error: {e}")
        time.sleep(TIEMPO)
