from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    datetime = models.DateField(auto_now=False)
    movie_type = models.ForeignKey(Type, on_delete=models.PROTECT)
    des = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='img/', null=True)
    capital = models.IntegerField()
    income = models.IntegerField()
    def __str__(self):
        return self.title

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    price =  models.IntegerField()
    movie_seat = models.ForeignKey(Movie, on_delete=models.PROTECT)
    seat_status = models.ForeignKey(Status, on_delete=models.PROTECT)