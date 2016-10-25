from django.conf import settings
from django.db import models


class CharityInstitution(models.Model):
    name = models.CharField(max_length=255)
    # TODO: address = 
    cnpj = models.CharField(max_length=14)


class News(models.Model):
    charity_institution = models.ForeignKey(
        CharityInstitution, related_name='news')
    text = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()


class Review(models.Model):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

    RATING_CHOICES = (
        (ONE_STAR, '1 star'),
        (TWO_STARS, '2 stars'),
        (THREE_STARS, '3 stars'),
        (FOUR_STARS, '4 stars'),
        (FIVE_STARS, '5 stars'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
    charity_institution = models.ForeignKey(
        CharityInstitution, related_name='reviews')
    date = models.DateTimeField()
    rating = models.SmallIntegerField(choices=RATING_CHOICES)
    text = models.TextField()

