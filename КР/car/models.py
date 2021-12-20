from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=64)
    yearFoundation = models.DateTimeField()
    chairman =  models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.name} - {self.yearFoundation} - {self.chairman}"
class Model(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,related_name="manufacturer")
    year =  models.DateTimeField()
    price =  models.IntegerField()
    weight =  models.IntegerField()
    euro5 =  models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.name} - {self.manufacturer} - {self.year} - {self.price} - {self.weight} - {self.euro5}"
        