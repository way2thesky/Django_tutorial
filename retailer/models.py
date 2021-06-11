from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, unique=True)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=50, unique=True)
    product = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
