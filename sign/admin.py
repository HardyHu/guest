# -*- coding: utf-8 -*-
from django.contrib import admin
from sign.models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_dispaly = ['id','name','status','address','start_time']
	search_fields = ['name']  #搜索栏
	list_filter = ['status']  #过滤器

class GuestAdmin(admin.ModelAdmin):
	list_dispaly = ['realname','phone','email','sign','create_time','event']
    list_display_links = ('realname','phone')
	search_fields = ['realname','phone']  #搜索栏
	list_filter = ['sign']                #过滤器

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
