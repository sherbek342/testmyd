from django.db import models

# Create your models here.
class Profile(models.Model):
    ptitle = models.CharField('Имя: ', max_length=20)

    def __str__(self):
        return self.ptitle
    
    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'
    