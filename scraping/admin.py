from django.contrib import admin

from .models import Author, Quote


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 5


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_title',
                    'author_born_date',
                    'author_born_location',
                    'author_description')
    fields = ['author_title',
              'author_born_date',
              ('author_born_location', 'author_description')]
    inlines = [QuoteInline]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author']
    search_fields = ['author']
    fields = ['quote']
