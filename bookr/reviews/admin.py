from django.contrib import admin
from .models import Publisher, Contributor, Book, BookContributor, Reviews


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names')
    list_filter = ('last_names',)


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13', 'has_isbn', 'get_publisher')
    list_filter = ('publisher', 'publication_date')
    search_fields = ['title', 'isbn', 'publisher__name']

    @admin.display(
        ordering='isbn',
        description='ISBN-13',
        empty_value='-/-',
    )
    def isbn13(self, obj):
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3],
                                       obj.isbn[3:4], obj.isbn[4:6],
                                       obj.isbn[6:12], obj.isbn[12:13])

    def get_publisher(self, obj):
        return obj.publisher.name

    @admin.display(
        boolean=True,
        description='Has ISBN',
    )
    def has_isbn(self, obj):
        return bool(obj.isbn)


# Register models with the admin site
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Reviews)
