from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=120,primary_key = True)
    real_name = models.CharField(max_length=120)
    tz = models.CharField(max_length = 120)
    
    def __str__(self):
        return str(self.id)

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    session_date = models.DateField(auto_now_add=False,auto_now=False)
    start_time = models.TimeField(auto_now_add=False,auto_now=False)
    end_time = models.TimeField(auto_now_add=False,auto_now=False)
    
    def __str__(self):
        return str(self.user)