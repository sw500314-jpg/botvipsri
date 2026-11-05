import telebot, os, glob
TOKEN = "9057029237:AAFAtQETgHSA35Ts6xUeYBP64h_JlyQUx9Q"
ADMIN_ID = 6383842005
bot = telebot.TeleBot(TOKEN)

files = glob.glob("*.jpg") + glob.glob("*.JPG") + glob.glob("*.png") + glob.glob("*.jpeg")
QRIS = None
VIP = None
for f in files:
    low = f.lower()
    if "vip" in low or "wa" in low or "img" in low:
        VIP = f
    else:
        if not QRIS:
            QRIS = f

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Halo sayang 😘 Transfer ke QRIS ini ya, kirim bukti kesini 💦")
    if QRIS and os.path.exists(QRIS):
        with open(QRIS,'rb') as q: bot.send_photo(m.chat.id,q)

@bot.message_handler(content_types=['photo','document','text'])
def bukti(m):
    if m.chat.id==ADMIN_ID: return
    bot.send_message(m.chat.id,"Bukti diterima 😘 tunggu dicek")
    bot.forward_message(ADMIN_ID,m.chat.id,m.message_id)
    bot.send_message(ADMIN_ID,f"ID:{m.chat.id} /acc {m.chat.id}")

@bot.message_handler(commands=['acc'])
def acc(m):
    if m.chat.id!=ADMIN_ID: return
    uid=int(m.text.split()[1])
    if VIP and os.path.exists(VIP):
        with open(VIP,'rb') as v: bot.send_photo(uid,v,caption="Welcome VIP sayang 😍")
    bot.send_message(m.chat.id,"ACC sukses")

bot.infinity_polling()
