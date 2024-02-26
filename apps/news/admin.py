from django.contrib import admin

from apps.news.models import New, User, Post, Categoriy


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoriy)
class CategoriyAdmin(admin.ModelAdmin):
    pass