from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from faker import Faker

UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Adding random Users/Email/Password.' # noqa A003

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(1, 11),
                            help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        objs = [
            UserModel(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username=fake.name(),
                email=fake.email(),
                password=make_password('Sample&Password!')
            )
            for _ in range(count)
        ]

        UserModel.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS('Successfully'))
