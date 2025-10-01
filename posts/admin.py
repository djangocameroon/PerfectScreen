from django.contrib import admin
from .models import SocialPost


@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ['username', 'platform', 'has_tagged_digitalocean', 'has_starred_repo', 'created_at']
    list_filter = ['platform', 'has_tagged_digitalocean', 'has_starred_repo']
    search_fields = ['username', 'post_url']
