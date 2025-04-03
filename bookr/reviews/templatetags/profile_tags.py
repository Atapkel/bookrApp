from reviews.models import Reviews
from django import template

register = template.Library()


@register.inclusion_tag('book_list.html')
def book_list(username):
    user_reviews = Reviews.objects.filter(creator__username__contains=username)
    books_read = [review.book.title for review in user_reviews]
    return {'books_read': books_read}
