from django.db import models
from django.contrib import auth

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50,
                            help_text="The name of the Publisher")
    website = models.URLField(
        help_text="The Publisher's website"
    )
    email = models.EmailField(
        help_text="The Publisher's email address"
    )
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=70, help_text="The title of the Book")
    publication_date = models.DateField(
        verbose_name="The publication date"
    )
    isbn = models.CharField(max_length=20, help_text="The ISBN number the of the Book")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT,
    )
    contributors = models.ManyToManyField(
        'Contributor', through='BookContributor',
    )
    def __str__(self):
        return self.title


class Contributor(models.Model):
    first_names = models.CharField(max_length=50, help_text="The first name of the Contributor")
    last_names = models.CharField(max_length=50, help_text="The last name of the Contributor")
    email = models.EmailField(help_text="The Contributor's email address")
    def __str__(self):
        return self.first_names

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
    )
    contributor = models.ForeignKey(
        Contributor, on_delete=models.CASCADE,
    )
    role = models.CharField(
        verbose_name="Contribution role",
        choices=ContributionRole.choices,
        max_length=20,
    )

class Reviews(models.Model):
    content = models.TextField(
        help_text="The review text")
    rating = models.IntegerField(
        help_text="The review rating")
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date the review was created")
    date_edited = models.DateTimeField(
        null=True,help_text="The date the review was edited")
    creator = models.ForeignKey(
        auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book the review was made")