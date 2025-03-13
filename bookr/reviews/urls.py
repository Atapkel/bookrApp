from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_details'),
    path('book-search/', views.book_search, name='book_search'),
    path("publishers/new/", views.publisher_edit, name="publisher_create"),
    path("publishers/new/<int:pk>/", views.publisher_edit, name="publisher_create"),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<pk>/media/', views.book_media, name='book_media'),

]

