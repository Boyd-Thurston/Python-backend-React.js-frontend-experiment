from django.db import models

# Create your models here.

class fruitbowl(models.Model):
  fruit = models.CharField(max_length=120)
  url = models.CharField(max_length=250)
  visable = models.BooleanField(default=False)

  def _str_(self):
    return self.fruit