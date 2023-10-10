from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from datetime import datetime

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=35)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_length=10, decimal_places=2, max_digits=20)
    auction = models.BooleanField("торг", help_text="Ответьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time=self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color:green; font-weight:bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='дата обновления')
    def updated_data(self):
        if self.updated_at.date() == datetime.now().date():
            updated_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color:#c08b72; font-weight:bold;"> Сегодня в {} </span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")


class Meta:
    db_table = 'advertisements'

def __str__(self):
    return f'<Advertisement: Advertisement(id={self.id}, title={self.price}, price={self.price: .2f})>'

