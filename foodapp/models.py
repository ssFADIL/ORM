from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=50)
    rating = models.FloatField()
    location = models.CharField(max_length=100)
    delivery_time = models.IntegerField()

    def __str__(self):
        return self.restaurant_name