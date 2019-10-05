from django.contrib import admin

# Register your models here.

from .models import UserFeedbackModel

class UserFeedbackAdmin(admin.ModelAdmin):

    pass

    

    



admin.site.register(UserFeedbackModel,UserFeedbackAdmin)
