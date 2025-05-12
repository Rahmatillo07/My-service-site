from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=25, verbose_name="Ism")
    telegram = models.CharField(max_length=15, verbose_name='telegram username')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
