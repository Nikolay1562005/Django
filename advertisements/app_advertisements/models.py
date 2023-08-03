from django.db import models


class Advertisement(models.Model):

    title = models.CharField("Название", max_length=128)  # короткие строки
    description = models.TextField('Описание')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)  # max_digits - цифр в числе (все) decimal_places - кол-во цифр после запятой
    auction = models.BooleanField("Торг", help_text="Укажите возможен ли торг")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price = {self.price})"

    class Meta:
        db_table = "advertisements"