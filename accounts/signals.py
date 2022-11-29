from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,UserProfile
from vender.models import Vender

@receiver(post_save,sender=User)
def post_save_user_profile(sender,instance,created,**kwargs):
    print(created)
    if created:
        #print("User profile is created")
        UserProfile.objects.create(user=instance)
        print("User and user profile is created")
    else:
        pass
        #try:
        #    profile = UserProfile.objects.create(user=instance)
        #    profile.save() 
        #except:
        #    UserProfile.objects.create(user=instance)
        #    print("User and profile is not found,so i created one")


