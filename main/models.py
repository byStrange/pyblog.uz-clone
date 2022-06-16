from tabnanny import verbose
from typing import OrderedDict
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):

    """
        Tags for posts
    """

    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    """
        Category model for Posts
    """

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):

    """
        main model for blog posts includes the following fields:
    """

    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Posts"

class Comments(models.Model):

    """
        comment section for each post
    """

    author = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Comments'

class Settings(models.Model):

    """
        Settings for social media links
    """

    telegram_link = models.URLField(max_length=50)
    instagram_link = models.URLField(max_length=50)
    facebook_link = models.URLField(max_length=50)
    twitter_link = models.URLField(max_length=50)

    def __str__(self):
        return {'telegram_link': self.telegram_link, 'instagram_link': self.instagram_link, 'facebook_link': self.facebook_link, 'twitter_link': self.twitter_link}