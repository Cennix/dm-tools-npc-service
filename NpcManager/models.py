from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class NpcDetails(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255, null=True, blank=True)
    title = models.CharField(max_length = 255, null=True, blank=True)

    age = models.PositiveIntegerField()
    race = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    is_alive = models.BooleanField(default=True)

    description = models.TextField()
    personality = models.TextField()
    notes = models.TextField(null=True, blank=True)

    creation_datetime = models.DateTimeField(auto_now_add = True)
    last_modified_datetime = models.DateTimeField(auto_now = True)

    @property
    def full_name(self):
        name = []
        if self.title: 
            name.append(self.title)
        name.append(self.first_name)
        if self.last_name:
            name.append(self.last_name)
        return " ".join(name)

    def __str__(self):
        return self.full_name


class NpcRelationshipMapper(models.Model):
    origin_npc = models.ForeignKey(NpcDetails, on_delete=models.CASCADE, related_name='origin_relationship')
    target_npc = models.ForeignKey(NpcDetails, on_delete=models.CASCADE, related_name='target_relationship')

    overview = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)

    event_age = models.PositiveIntegerField()
    ongoing = models.BooleanField(default=True)
    weighting = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(-5)])

    def __str__(self):
        return f"{self.origin_npc} {self.overview} {self.target_npc}"
