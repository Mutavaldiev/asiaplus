
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(models.Model):
    STATUS = [("draft", "Draft"),("published", "Published"),]
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="articles/",blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="articles")
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name="articles")
    status = models.CharField(max_length=20,choices=STATUS,default="draft")
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    STATUS = [ ("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected"),]
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.article.title}"

    class Meta:
        ordering = ["-created_at"]


class EmailConfirm(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="email_codes")
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
