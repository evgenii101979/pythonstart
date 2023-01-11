import requests
from bs4 import BeautifulSoup

url = 'https://www.banki.ru/products/currency/cash/nizhniy_novgorod/' # вставляем урл сайта 
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') # получаем текст страницы, через гугл-код-смотрим подсветку и копи код
#print(soup)
mass = soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-left-default')
print(mass)
string = str(soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-left-default')[1])
print(string)
print(string[string.find('>')+1:string.find('</div>'):].replace(',', '.'))
