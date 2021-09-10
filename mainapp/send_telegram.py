import requests

def send_telegram(user,phone: str):
    text = f'Заказ от имени {user} телефон {phone}'
    token = "1720804384:AAFIORNXJ9HZTqskrwiqfVUrzrxhjxEglcQ"
    url = "https://api.telegram.org/bot"
    channel_id = "147334106"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
    data = 'Клиент - Петров\nТелефон\n89269286687'
    send_telegram(data)