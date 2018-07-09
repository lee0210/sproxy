from django.db import models

class Heartbeat(models.Model):
    app_name = models.CharField(max_length=50)
    last_beat = models.DateTimeField()
