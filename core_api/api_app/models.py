from django.db import models

# Create your models here.


class Key_word(models.Model):
    key_word = models.CharField(max_length=100, db_index = True)
    videos = models.CharField(max_length=100000, blank=True, null=True)
    create_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.key_word
