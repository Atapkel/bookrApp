from django import forms
from .models import Publisher, Reviews, Book

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ('date_edited','book')
        rating = forms.IntegerField(min_value=0, max_value=5)



CHOICES = (
    ['contributor', 'Contributor'],['title','Title']
)

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.Textarea, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=CHOICES)

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["cover", "sample"]