from django.db import models
from django.utils.html import format_html

class ProductsModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def picture(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%" />'.format(self.image.url))
    
class InfoModel(models.Model):
    admin_telegram_username = models.CharField(max_length=50)
    admin_phone_number = models.CharField(max_length=20)
    bot_username = models.CharField(max_length=50)

    def __str__(self):
        return self.admin_telegram_username

class UsersModel(models.Model):
    username = models.CharField(max_length=50, null=True)
    telegram_id = models.CharField(max_length=20)
    lang = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.username
