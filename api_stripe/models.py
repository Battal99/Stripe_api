from django.db import models


class Item(models.Model):
    __tablename__ = "Item"

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}, {self.price}"
