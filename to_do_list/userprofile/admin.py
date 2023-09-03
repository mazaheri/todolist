from django.contrib import admin
from userprofile.models import Category, Task
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    list_filter = ['user']
    ordering = ['-user']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Task)