from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo(models.Model):
    
    SHOPPING = "Shopping"
    WORK = "Work"
    ENTERTAIN = "Entertain"
    FAMILY = "Family"
    UNKNOWN = "Unknown"
    TODO_TYPES = {
        SHOPPING : "Shopping",
        WORK: "Work",
        ENTERTAIN: "Entertain",
        FAMILY: "Family",
        UNKNOWN: "Unknown",
    }
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=20, choices=TODO_TYPES, default="Unknown")
    status = models.BooleanField(default=False)
    deadline = models.DateField(default=date.today)
    created_at = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name
    