from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from .forms import BookForm
from .models import Book
# Create your views here.


class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record deleted successfully")


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete_form.html'
    success_url = '/book_management/delete_success/'



class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'

class BookRecordDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    success_url = '/book_management/entry_success'



class BookRecordFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = '/book_management/entry_success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully")