import requests

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# for i in res.values():
#     print(i)
print(res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value'])
print(res['Valute']["EUR"]['Name'], res['Valute']["EUR"]['Value'])
print(res['Valute']["GBP"]['Name'], res['Valute']["GBP"]['Value'])
print(res['Valute']["BYN"]['Name'], res['Valute']["BYN"]['Value'])