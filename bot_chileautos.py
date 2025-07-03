import os, requests, time
from bs4 import BeautifulSoup
from telegram import Bot

# Configuración
TOKEN = os.getenv('TOKEN')
CHAT = os.getenv('CHAT')
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
            bot.send_message(chat_id=CHAT, text=f'🚗 {titulo}\n🔗 https://www.chileautos.cl{link}')

while True:
    revisar()
    time.sleep(TIEMPO)
