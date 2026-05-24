
# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
models.py
```
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
```
admin.py
```
from django.contrib import admin
from .models import Restaurant

admin.site.register(Restaurant)
```
apps.py
```
from django.apps import AppConfig


class FoodappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodapp'

```



## OUTPUT

c:\Users\acer\OneDrive\Pictures\Screenshots\Screenshot 2026-05-22 110332.png


## RESULT
Thus the program for creating a database using ORM hass been executed successfully 
