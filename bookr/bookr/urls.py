from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.contrib.auth import views
# from bookr_admin.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path("accounts/password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done", ),
    path("accounts/reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
    path('filter_demo/', include('filter_demo.urls')),
    path('book_management/',include('book_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
