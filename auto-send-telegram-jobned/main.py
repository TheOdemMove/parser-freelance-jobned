import datetime
import time
import re
import html2text
import requests
import telebot
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
bot = telebot.TeleBot('610361295:AAFmhfsnFGF2rJTUxL15m05UXJZBIhAl-eA')
filter = ['bot', 'telegram', 'python', 'django', 'flask', 'вёрстка', 'c++', 'программу', 'бот', 'телеграм', 'вайбер', 'рассылка', 'arduino', 'deploy', 'автоматизация', 'скрипт', 'mysql', 'base', 'база даных', 'парсер', 'парсинг']

######

def send_new_card(name_card, desc_card):
    bot.send_message(487348303, name_card + '\n\n' + desc_card)


def parse_html():
    count = 0
    while True:
        count += 1
        cook = {'PHPSESSID': 'rqtl198s9r17k8nnnodj0o09k8'}
        header = {'Host': 'jobned.com',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                  'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
                  'DNT': '1',
                  'Alt-Used': 'jobned.com',
                  'Connection': 'keep-alive',
                  'Upgrade-Insecure-Requests': '1',
                  'Cache-Control': 'max-age=0',
                  'TE': 'Trailers'
                  }
        try:
            r = requests.get("https://jobned.com/components/list_load.php", cookies=cook, headers=header, verify=False,
                             timeout=30)
            if count > 1:
                data_new = r.json()
                if data == data_new:
                    print("Нових не знайдено, спроба №", count)
                else:
                    print("Знайдено нове завдання, перевіряємо його на наявність слів з вашого фільтру....")
                    for i in data_new:
                        if i in data:
                            pass
                        else:
                            send_test(i)

                    data = r.json()
            else:
                data = r.json()
                print("New Page")
            time.sleep(4)
        except Exception as e:
            print(e)
            time.sleep(4)


def send_test(i):
    date_now = datetime.datetime.now()
    date_now = str(date_now.strftime("%d.%m.%y %H:%M:%S"))
    desc = html2text.html2text(i['text'])

    for poisk in filter:
        if poisk in desc.lower():
            print("Знайшли слова з вашого фільтру: {}".format(poisk))
            if 'за домовленістю' in str(i['price_text']):
                price = 'за домовленістю'
            else:
                all_price = re.findall(r'\d+', i['price_text'])
                price = all_price[0]

            if 'fl.ru' in str(i['b_name']).lower():
                head = 'FL'
            elif 'freelancehunt' in str(i['b_name']).lower():
                head = 'FH'
            elif 'habr' in str(i['b_name']).lower():
                head = 'HABR'
            elif 'weblancer' in str(i['b_name']).lower():
                head = 'WL'
            elif 'freelance.ru' in str(i['b_name']).lower():
                head = 'F.ru'
            elif 'freelance.youdo' in str(i['b_name']).lower():
                head = 'FL-YD'
            elif 'upwork' in str(i['b_name']).lower():
                head = 'UpW'
            elif 'freelancer.com' in str(i['b_name']).lower():
                head = 'F.com'
            elif 'peopleperhour' in str(i['b_name']).lower():
                head = 'PPH'
            elif 'guru' in str(i['b_name']).lower():
                head = 'GURU'
            elif 'etxt' in str(i['b_name']).lower():
                head = 'eTXT'
            elif 'youdo' in str(i['b_name']).lower():
                head = 'YD'
            elif 'freelance.ua' in str(i['b_name']).lower():
                head = 'F.ua'
            elif 'text.ru' in str(i['b_name']).lower():
                head = 'TXT'
            elif 'advego' in str(i['b_name']).lower():
                head = 'ADVG'
            elif 'kabanchik' in str(i['b_name']).lower():
                head = 'KB'
            elif 'kwork' in str(i['b_name']).lower():
                head = 'KWORK'
            else:
                head = 'NONE'

            llink = 'https://jobned.com/redirect/' + str(i['id'])
            namecard = head + ' | ' + str(i['name'])
            msg = "🔹 Описание:\n{}\n🔹 Цена: {}\n🔹 Время: {}\n🔹 Биржа и категория: {} | {}\n🔹 Ссылка: {}".format(desc, price, date_now, i['b_name'],i['cats'],llink)
            send_new_card(namecard, msg)
            break
        else:
            #print("Слова з вашого фільтру не співпадають, пропускаємо це завдання...")
            pass
    # print(i)


if __name__ == '__main__':
    parse_html()
