from signal import SIGPIPE, SIG_DFL, signal

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Author, Quote

signal(SIGPIPE, SIG_DFL)


@shared_task
def scraping_quotes():
    # собираем html
    page = requests.get('https://quotes.toscrape.com')
    quote_for_scrap = 0
    while quote_for_scrap < 5:
        # преобразуем в soup-объект
        soup = BeautifulSoup(page.content, features='xml')
        # собираем все посты
        quotes = soup.findAll('div', {'class': 'quote'})

        for i in quotes:
            text = i.find('span', {"class": "text"}).text

            if not Quote.objects.filter(quote_text=text).exists():
                author_url = requests.get('https://quotes.toscrape.com' + i.find('a').get('href'))
                author_soup = BeautifulSoup(author_url.content, features='xml')
                author_detail = author_soup.find('div', class_='author-details')

                auth = author_detail.find('h3', class_='author-title').text

                if not Author.objects.filter(author_title=auth).exists():
                    author_born_date = author_detail.find('span', class_='author-born-date').text
                    author_born_location = author_detail.find('span', class_='author-born-location').text
                    author_description = author_detail.find('div', class_='author-description').text

                    author = Author.objects.create(author_title=auth,
                                                   author_born_date=author_born_date,
                                                   author_born_location=author_born_location,
                                                   author_description=author_description)
                else:
                    author = Author.objects.get(author_title=auth)

                quote = Quote.objects.create(quote_text=text, author=author)
                quote.save()

                quote_for_scrap += 1
                if quote_for_scrap == 5:
                    break

        find_link = soup.find('li', {'class': 'next'})
        if not find_link:
            # проверяем что это последняя цитата
            last_quote = quotes[-1].find('span', {"class": "text"}).text
            if Quote.objects.filter(quote_text=last_quote):
                send_mail(
                    subject='All quotes added in DataBase',
                    message='All done',
                    from_email='example@example.com',
                    recipient_list=['admin@admin.com'],
                )
                break
            break

        link = find_link.a.get('href')
        page = requests.get('https://quotes.toscrape.com' + link)
