# from celery import shared_task
# from bs4 import BeautifulSoup
#
# from urllib.request import urlopen
#
#
# @shared_task
# def scrap_quote():
#     all_quotes = []
#     for i in range(1, 6):
#         url = f'https://quotes.toscrape.com/page/{i}/'
#         page = urlopen(url)
#         soup = BeautifulSoup(page, 'html.parser')
#         quotes = soup.find_all('div', class_='quote')
#
#         for quote in quotes:
#             text = quote.find('span', class_='text').text
#             author = quote.find('small', class_='author').text
#             tags = quote.find('div', class_='tags').find_all('a')
#
#             tags_list = []
#             for tag in tags:
#                 tags_list.append(tag.text)
#
#             single_quote = [text, author, tags_list]
#             all_quotes.append(single_quote)
