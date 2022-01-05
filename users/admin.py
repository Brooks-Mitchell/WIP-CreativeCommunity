from django.contrib import admin

from users.models import Profile
from .models import Profile

admin.site.register(Profile)
