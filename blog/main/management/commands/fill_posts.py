# import requests
# from bs4 import BeautifulSoup
#
# from django.core.management.base import BaseCommand
#
#
# class Command(BaseCommand):
#
#     def parser(self):
#         url = 'https://sportschools.ru/page.php?name=items'
#         page = requests.get(url)
#         print(str(page.status_code) + ' ' + 'status')
#
#         soup = BeautifulSoup(page.text, "html.parser")
#
#         a = []
#         title_article = []
#
#         allArticle = soup.find_all('div', 'a', class_='box')
#         # c = soup.findAll('a')
#         # print(allArticle)
#
#         article_link = soup.find('div', {'class': 'box'})
#         print(article_link)
#
#         # for data in c:
#         #     if data.find('strong') is not None:
#         #         title_article.append(data.text)
#         #
#         # print(title_article)
