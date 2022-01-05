from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()




# docs

# When a user is saved, send a signal
# signal will be recieved and create profile
# instance is the user that is creating a profile


# 11/26 note: 
# Might use signals for when studio is created to automatically put creator in the studio, plus make an auto post
