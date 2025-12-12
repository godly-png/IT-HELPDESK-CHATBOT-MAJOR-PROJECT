from django.contrib import admin
from .models import UserProfile   # keep only models that actually exist

admin.site.register(UserProfile)

