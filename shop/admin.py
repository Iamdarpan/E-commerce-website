from django.contrib import admin
from .models import container,post 

class containerAdmin(admin.ModelAdmin):
    list_display = ('container_image','container_title','container_des','container_url',)
    list_filter = ('container_title',)
    search_fields = ('container_title',)


class postAdmin(admin.ModelAdmin):
    list_display = ('post_title',)
    list_per_page = 20
    list_filter = ('post_title',)

# Register your models here.
admin.site.register(container,containerAdmin)
admin.site.register(post,postAdmin)