from django.db.models.signals import post_save   # this signal gets fired after an object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)   # = When a user is saved or created, then send 'post_save' signal, received by 'receiver who is create_profile function'
def create_profile(sender, instance, created, **kwargs):   #arguments passed by 'post_save' signal **kwargs only accepts any additional keyword arguments
    if created:                                            # if the user was createed
        Profile.objects.create(user=instance)              # then create a profile object with the "user=instance if the user created"



@receiver(post_save, sender=User)                           # saves the profile
def save_profile(sender, instance,**kwargs): 
    instance.profile.save() 