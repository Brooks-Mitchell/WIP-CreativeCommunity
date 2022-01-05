from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# this is the user profile with just a name and profile pic

class Profile(models.Model):

    ROLE_OPTIONS = (
        ('animator', 'Animator'),
        ('scriptwriter', 'Scriptwriter'),
        ('audio engineer', 'Audio Engineer'),
        ('graphic design', 'Graphic Design'),
        ('videographer', 'Videographer'),
        ('video editor', 'Video Editor'),
        ('none', 'None')
    )

    COMMITMENT_LEVEL = (
        ('casual', 'Casual'),
        ('side project', 'Side Project'),
        ('1 priority', '#1 Priority')
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_bio = models.TextField(max_length=320, default="", blank=True)
    user_yoe = models.IntegerField(default=0)
    user_role = models.CharField(max_length=80, choices=ROLE_OPTIONS, default='none')
    user_commitment_level = models.CharField(max_length=80, choices=COMMITMENT_LEVEL, default='Casual')
    # next to add are tools and if a studio, as well as remaining role positions

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
