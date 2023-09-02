from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(MyUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
# admin.site.register(Cart)
