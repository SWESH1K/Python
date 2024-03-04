from datetime import *
from pytz import *
from telegram import *
from telegram.ext import *

birthday = {
    "25-05":["Ashwin"],
    "04-11":["Nipun"],
    "30-05":["Yeshwanth"],
    "11-12":["Sayooj"],
    "1-03":["Nawaz"]
}

today = datetime.now(timezone('Asia/kolkata'))
today_str = today.strftime("%d-%m")
print(today_str)
  
API_key = "6703139595:AAEjDf_X2zaREdi1_KDemyUFqwpmsRmC4Jk"
Chat_Id = "5918013737"

bot = Bot(API_key)
update = Updater(API_key, use_context = True)
update.start_polling()
if today_str in birthday:
    message = "B'Day notification\n"
    for i in birthday[today_str]:
        message += i +'\n'
    print(message)
