from django.db import models

# Create your models here.


class Buyer(models.Model):                                          #  Модель покупателя

    name = models.CharField(max_length=100)                         # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс (10 цифр, 2 знака после запятой)
    age = models.IntegerField()                                     # Возраст (Только целые числа)

    def __str__(self):                       # Метод для строкового представления объекта
        return self.name                     # Возвращаем имя покупателя

class Game(models.Model):                                           #  Модель игры

    title = models.CharField(max_length=100)                        # Название игры (100 символов)
    cost = models.DecimalField(max_digits=10, decimal_places=2)     # Цена (10 цифр, 2 знака после запятой)
    size = models.DecimalField(max_digits=10, decimal_places=2)     # Размер файлов игры
    description = models.TextField()                                # Описание (неограниченное количество символов)
    age_limited = models.BooleanField(default=False)                # Ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer)     # Покупатель обладающий игрой

    def __str__(self):                       # Метод для строкового представления объекта
        return self.title                    # Возвращаем название игры

"""
Создание миграций для новых моделей
python manage.py makemigrations

Применение миграций к db.sqlite3
python manage.py migrate
"""
