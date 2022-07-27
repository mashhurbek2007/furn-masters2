from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Login)
admin.site.register(Buy)
admin.site.register(Discover)