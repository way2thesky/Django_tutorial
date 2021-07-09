from celery import shared_task
from bs4 import BeautifulSoup
import requests
from django.core.mail import send_mail
from .models import Author, Quote
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)


@shared_task
def scraping_quotes():
    # собираем html
    page = requests.get('https://quotes.toscrape.com')
    quote_for_scrap = 0
    while True:
        # преобразуем в soup-объект
        soup = BeautifulSoup(page.content, features='html.parser')
        # собираем все посты
        quotes = soup.findAll('div', {'class': 'quote'})

        for i in quotes:
            quote = i.find('span', {"class": "text"}).text
            author_url = requests.get('https://quotes.toscrape.com' + i.find('a').get('href'))
            author_soup = BeautifulSoup(author_url.content, features='html.parser')
            auth, temp = Author.objects.get_or_create(author_title=i.find('small', class_='author').text,
                                                      author_born_date=author_soup.find('span',
                                                                                        class_='author-born-date').text,
                                                      author_born_location=author_soup.find('span',
                                                                                            class_='author-born'
                                                                                                   '-location').text,
                                                      author_description=author_soup.find('div',
                                                                                          class_='author-description').text)

            if not Quote.objects.filter(quote_text=quote).exists():
                Quote.objects.get_or_create(quote_text=quote, author=auth)
                quote_for_scrap += 1
            if quote_for_scrap == 5:
                return

        find_link = soup.find('li', {'class': 'next'})
        if not find_link:
            send_mail(
                subject='All quotes added in DataBase',
                message='All done',
                from_email='example@example.com',
                recipient_list=['admin@admin.com'],
            )
            break

        link = find_link.a.get('href')
        page = requests.get('https://quotes.toscrape.com' + link)
