from django.db import models

class NpcDetails(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255, null=True, blank=True)

    age = models.PositiveIntegerField()
    race = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    is_alive = models.BooleanField(default=True)

    description = models.TextField()
    personality = models.TextField()
    notes = models.TextField()

    creation_datetime = models.DateTimeField(auto_now_add = True)
    last_modified_datetime = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        if self.title: 
            name = self.title + " " + name
        return name
