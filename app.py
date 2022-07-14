import botogram, requests, json

bot = botogram.create("YOUR-KEY-BOT")



@bot.command("start")
def start_command(chat, message):
    cari = "ini cari"
    coba = "ini juga coba"
    user = botogram.User()
    chat.send("\n {} \n {} \n {}".format(cari,coba, user))
    


@bot.command("search")
def search_command(chat, message, args):
    btns = botogram.Buttons()
    btns[0].callback("Transaction Data", "transaksi")
    btns[1].callback("User Data", "user")

    chat.send("What are you looking for?", attach=btns)

@bot.callback("transaksi")
def notify_callback(query, data, chat, message):
    url = 'YOUR-API'
    response_info = requests.get(url)
    response = response_info.json()

    data_j = response['result']

    for i in data_j:
        lis = []
        User = i['user']
        Amount = i['amount']
        Va = i['va']
        transaction_id = i['transaction_id']
        payment_method = i['payment_method']
        payment_status =i['payment_status']
        datetime = i['datetime']
        lis.append(i)
        chat.send("Transaction ID : {} \n User : {} \n VA : {} \n Amount : {} \n Payment Method : {} \n Payment Status {} \n DateTime : {} \n ".format(transaction_id, User, Va, Amount, payment_method, payment_status, datetime))
    chat.send("Return to the search menu, type /start.")


@bot.callback("user")
def callback_user(query, data, chat, message):
    url = 'YOUR-API'
    response_info = requests.get(url)
    response = response_info.json()


    data_j = response['result']

    for i in data_j:
        lis = []
        id_user = i['id']
        Name = i['name']
        Address = i['address']
        Phone_Number = i['phone_number']
        lis.append(i)
        chat.send("ID User : {} \n Name : {} \n Address : {} \n Phone Number : {} \n".format(id_user, Name, Address, Phone_Number))
    chat.send("Return to the search menu, type /start.")


@bot.command("CekVa")
def hello_command(chat, message, args):
    url = "YOUR-API"
    PARAMS = {"va": args}

    json_data = requests.get(url, params = PARAMS)



    response = json_data.json()
    data_j = response['result']


    for i in data_j:
        lis = []
        User = i['user']
        Amount = i['amount']
        Va = i['va']
        transaction_id = i['transaction_id']
        payment_method = i['payment_method']
        payment_status =i['payment_status']
        datetime = i['datetime']
        lis.append(i)
        chat.send("Transaction ID : {} \n User : {} \n VA : {} \n Amount : {} \n Payment Method : {} \n Payment Status {} \n DateTime : {} \n ".format(transaction_id, User, Va, Amount, payment_method, payment_status, datetime))
    chat.send("Return to the search menu, type /start.")



if __name__ == "__main__":
    bot.run()