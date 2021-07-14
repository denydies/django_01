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
#         print(soup)
#
