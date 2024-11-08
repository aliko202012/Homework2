from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    created = models.DateTimeField(
            auto_now_add=True
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Оснавная настройка сайта'
        verbose_name_plural = 'Основные настройки сайта'