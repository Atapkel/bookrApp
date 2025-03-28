"""bookr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from reviews.admin import admin_site
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path("accounts/password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done", ),
    path("accounts/reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
