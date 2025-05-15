from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
     Register=models.IntegerField(primary_key="Register");
     bookname=models.CharField(max_length=20);
     publisher=models.CharField(max_length=20);
     Dop=models.DateField();
     pages=models.IntegerField();
class Book_DBAdmin(admin.ModelAdmin):
     list_display=("Register","bookname","publisher","Dop","pages");


