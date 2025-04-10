from django.urls import path, include
from . import views, api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)

urlpatterns = [
    path('api/login', api_views.Login.as_view(), name='login'),
    path('api/', include((router.urls, 'api'))),
    # path('api/contributors/', api_views.AllContributors.as_view(),name='allcontributors'),
    # path('api/all_books/', api_views.AllBooks.as_view(), name='first_api_view'),
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile, name='profile'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_details'),
    path('book-search/', views.book_search, name='book_search'),
    path("publishers/new/", views.publisher_edit, name="publisher_create"),
    path("publishers/new/<int:pk>/", views.publisher_edit, name="publisher_create"),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<pk>/media/', views.book_media, name='book_media'),

]
