from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


# class Category(models.Model):
#     pass


class Categories(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"


class Review(models.Model):
    comment = models.TextField()
    attachment = models.FileField(upload_to='movie/attachment/review', null=True, blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{} - Review '.format(self.movie.name)


class Movie(models.Model):  # My table in the database

    # slug = models.SlugField()
    active = models.BooleanField(default=True)

    name = models.CharField("Movie Name", max_length=255, unique=True)  # my first column in the table

    description = models.TextField(verbose_name="Movie Description")

    likes = models.IntegerField(default=0, null=True)

    watch_count = models.IntegerField(default=0, null=True)

    rate = models.PositiveIntegerField(default=0, null=True)

    production_date = models.DateField(null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    poster = models.ImageField(upload_to='movie/movie/images')

    video = models.FileField(upload_to='movie/movie/videos')

    actors = models.ManyToManyField("Actor")

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='movie/actor/images')

    id_name = models.OneToOneField("IdNumber", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('id',)
        verbose_name = "Cast"
        verbose_name_plural = "Casts"


class IdNumber(models.Model):
    number = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.number


class AttachmentCommon(models.Model):
    name = models.CharField(max_length=50)
    location = models.FileField()

    class Meta:
        abstract = True


class MyImageClass(AttachmentCommon):
    content = models.CharField(max_length=50)


class MyVideoClass(AttachmentCommon):
    content = models.CharField(max_length=50)
