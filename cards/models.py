from django.db import models
from django.contrib.auth.models import User



CARD_STATUS = (
    ('Неактивована','Неактивована'),
    ('Активована','Активована'),
    ('Прострочена','Прострочена'),
   
)

# Create your models here.
class Card(models.Model):
    series = models.CharField(max_length=100)
    number = models.CharField(max_length=16, unique=True)
    date_of_issue = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    date_of_use =  models.DateField()
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=CARD_STATUS)

    model_photo = models.ImageField()
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.series

    def snippet(self):
        return self.number
