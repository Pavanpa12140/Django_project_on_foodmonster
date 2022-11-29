from django.db import models
from accounts.models import User,UserProfile
# Create your models here.

class Vender(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    User_profile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    vender_name = models.CharField(max_length=200)
    vender_liciense = models.ImageField(upload_to = 'user/liciense',blank=True)
    is_approved = models.BooleanField(blank=True,null=True)
    created_date = models.DateField(blank=True,null=True)
    modified_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.vender_name
