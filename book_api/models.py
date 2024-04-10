from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_page = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()
    
    
    def __str__(self) -> str:
        return self.title
