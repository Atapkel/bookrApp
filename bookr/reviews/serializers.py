from rest_framework import serializers
from .models import Book, Publisher, BookContributor, Contributor, Reviews
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    book = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reviews
        fields = ['pk', 'content', 'date_created', 'date_edited', 'rating', 'creator', 'book', 'book_id']

    def create(self, validated_data):
        request = self.context["request"]
        creator = request.user
        if not creator.is_authenticated:
            raise NotAuthenticated('Authentication required.')
        book = Book.objects.get(pk=request.data['book_id'])
        return Reviews.objects.create(content=validated_data['content'], book=book, creator=creator,
                                     rating=validated_data['rating'])

    def update(self, instance, validated_data):
        request = self.context['request']
        creator = request.user
        if not creator.is_authenticated or instance.creator_id != creator.pk:
            raise PermissionDenied('Permission denied, you are not the creator of this review')
        instance.content = validated_data['content']
        instance.rating = validated_data['rating']
        instance.date_edited = timezone.now()
        instance.save()
        return instance


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']

class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher']

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookContributor
        fields = ['book','role']

class ContributorSerializer(serializers.ModelSerializer):
    bookcontributor_set = ContributionSerializer(read_only=True, many=True)
    number_contributions = serializers.ReadOnlyField()
    class Meta:
        model = Contributor
        fields = ['first_names', 'last_names','email',
                  'bookcontributor_set','number_contributions']