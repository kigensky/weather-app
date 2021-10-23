from django.db import models
from django.db.models.enums import Choices

Days = (
    (0, "Sunday"),
    (1, "Monday"),
    (2, "Teusday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday")
)

class Measurements(models.Model):
    Days_of_the_week = models.IntegerField(choices=Days, default=0)
    Rainfall = models.FloatField()
    Day_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-Day_created']

    def __str__(self):
        return str(self.Day_created)

