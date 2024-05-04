from django.contrib import admin

# from .models import Object, Relationship
from .models import Article



# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#
#
# @admin.register(Object)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'image']
    list_filter = ['id', 'published_at']
    search_fields = ['title',]



