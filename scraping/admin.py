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
                    'author_about')
    fields = ['author_title',
              'author_born_date',
              ('author_born_location', 'author_about')]
    inlines = [QuoteInline]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote_text', 'author']
    search_fields = ['author']
    fields = ['quote_text']
