from django.contrib import admin
from .models import User, SupportTicket

# Register your models here.
admin.site.register(User)
admin.site.register(SupportTicket)