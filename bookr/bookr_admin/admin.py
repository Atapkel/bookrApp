from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

class BookrAdmin(admin.AdminSite):
  site_header = "Bookr Administration"
  site_title = "Bookr Administration"
  index_title = "Bookr Administration"
  logout_template = "admin/logout.html"

  def profile_views(self, request):
      request.current_app = self.name
      context = self.each_context(request)
      return TemplateResponse(request, 'admin/admin_profile.html', context)

  def get_urls(self):
      urls = super().get_urls()
      urlpatterns = [
          path('admin_profile',self.admin_view(self.profile_views))
      ]
      return urlpatterns + urls

  def each_context(self, request):
      context = super().each_context(request)
      context['username'] = request.user.username
      return context

