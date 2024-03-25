from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
