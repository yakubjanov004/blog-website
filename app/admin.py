from django.contrib import admin
from .models import Profile,Service,Blog,Skill,Category,About,Project
# Register your models here.


@admin.register(Profile)
class Profile_admin(admin.ModelAdmin):
    list_display = ('full_name', 'bio')
    list_display_links = ('full_name', 'bio')
    search_fields = ('full_name',)

@admin.register(Service)
class Service_admin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order')
    list_display_links = ('name', 'icon', 'order')
    search_fields = ('name',)

@admin.register(Blog)
class Blog_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description')
    list_display_links = ('title', 'author', 'description')
    search_fields = ('title', 'author',)

@admin.register(Skill)
class Skill_admin(admin.ModelAdmin):
    list_display = ('name', 'order', 'percentage')
    list_display_links = ('name', 'order', 'percentage')
    search_fields = ('name', 'order',)

@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(About)
class About_admin(admin.ModelAdmin):
    list_display = ('body', 'amount', 'project_count', 'customer_count')
    list_display_links = ('body', 'amount', 'project_count', 'customer_count')
    search_fields = ('body', 'amount',)

@admin.register(Project)
class Project_admin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'description')
    list_display_links = ('name', 'category_id', 'description')
    search_fields = ('name', 'description',)

