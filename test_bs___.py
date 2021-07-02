# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://sportschools.ru/page.php?name=items'
# page = requests.get(url)
# print(str(page.status_code) + ' ' + 'status')
#
# soup = BeautifulSoup(page.text, "html.parser")
# # print(soup)
#
# a = soup.find_all('a')
#
# for i in a:
#     print(i.text)
