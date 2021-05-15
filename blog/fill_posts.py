# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://doroshenkoaa.ru/med/'
#
#
# def get_html(url, params=''):
#     response = requests.requests.get(url)
#     return response
#
#
# def get_content(html):
#     soup = BeautifulSoup(response.content, 'html.parser')
#     items = soup.find_all('h2')
#
#     data = []
#     for item in items:
#         data.append(
#             {
#                 'title': item.find('h2', class='title').get_text(strip=True)
#             }
#         )
#
#
# response = requests.get(url)
# soup_page = BeautifulSoup(response.content, 'html.parser')
# article_title = soup_page.find_all('h2')
# # article_title.text.strip('a')
# # cur = soup_page.findAll()
# print(article_title)
