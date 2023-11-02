from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone
from django.utils.safestring import mark_safe
User = get_user_model()


class advertisement(models.Model):
    title = models.CharField('заголовок', max_length=255)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте,если торг уместен')
    created_at = models.DateTimeField('дата', auto_now_add=True)
    updated_at = models.DateTimeField('обновлённая дата', auto_now=True)
    image = models.ImageField('изображение', upload_to='advertisments/', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null=True, default=None)
    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: purple; font=weight : bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d-%m-%Y %H:%M:%S")

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font=weight : bold;">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y %H:%M:%S")








    class Meta:
        db_table = 'advertisement'

    def __str__(self):
        return f'<advertisement: advertisement(id={self.id}, title={self.title}, price={self.price:.2f})>'


    def get_absolute_url(self):
        return reverse('tov-detail', kwargs={'pk': self.pk})