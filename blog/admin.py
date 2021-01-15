from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display  = ('title','author')


class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'description')
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)