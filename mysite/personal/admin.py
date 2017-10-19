# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "date"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated","date"]
	search_fields = ["title","content"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)

# Register your models here.
