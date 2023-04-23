from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Url(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_url = models.URLField()
    alias = models.CharField(max_length=8, blank=True, null=True, unique=True)
    timestamp = models.DateTimeField(auto_now=True)
    redirect_count = models.IntegerField(default=0)
    last_clicked = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("-timestamp",)
