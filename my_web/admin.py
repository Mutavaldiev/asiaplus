
from django.contrib import admin
from .models import Category, Article, Comment, EmailConfirm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ("title","category","author","status","views","created_at",)
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description", "content")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("views", "created_at", "updated_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("user","article","status","created_at",)
    list_filter = ("status", "created_at")
    search_fields = ("text", "user__username")
    actions = ["approve_comments"]
    @admin.action(description="Approve selected comments")
    def approve_comments(self, request, queryset):
        queryset.update(status="approved")


@admin.register(EmailConfirm)
class EmailConfirmAdmin(admin.ModelAdmin):

    list_display = ("user","code","created_at","expires_at","is_used",)
    readonly_fields = ("created_at",)
