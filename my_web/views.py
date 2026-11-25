from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from random import randint
from django.utils import timezone
from datetime import timedelta
from .models import Category, Article, Comment, EmailConfirm



def home(request):
    articles = Article.objects.filter(status="published").select_related("category", "author")
    categories = Category.objects.all()
    context = {"articles": articles[:12],"categories": categories,}
    return render(request, "home.html", context)




def article_list(request):
    articles = Article.objects.filter( status="published").select_related("category", "author")
    category = request.GET.get("category")
    if category:
        articles = articles.filter( category__slug=category)
    return render(request,"home.html",{"articles": articles,"categories": Category.objects.all(),})





def article_detail(request, slug):
    article = get_object_or_404( Article, slug=slug, status="published")
    Article.objects.filter(id=article.id).update(views=F("views") + 1)
    article.refresh_from_db()
    comments = Comment.objects.filter( article=article, status="approved").select_related("user")
    return render(request,"article_detail.html",{"article": article,"comments": comments,})







def registration(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if User.objects.filter(username=username).exists(): 
            return render(request, "registration.html")
        user = User.objects.create_user( username=username, email=email, password=password, is_active=False)
        code = str(randint(100000, 999999))
        subject = "Asia Plus | Email Verification"

        message = f"""
Hello {username},

Welcome to Asia Plus!

Your verification code is: {code}

Best regards,
Asia Plus Team
"""
        from django.conf import settings
        email_message = EmailMultiAlternatives( subject, message, settings.DEFAULT_FROM_EMAIL, [user.email] )
        email_message.send()
        return redirect('confirm_email')
    return render(request, "registration.html")






def confirm_email(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        code = request.POST.get("code", "").strip()
        user = User.objects.filter(username=username,is_active=False).first()
        if not user:
            return render(request, "confirm_email.html", {"error": "User not found"})
        code_obj = EmailConfirm.objects.filter(user=user,code=code,is_used=False,expires_at__gt=timezone.now()).first()
        if code_obj:
            user.is_active = True
            user.save()
            code_obj.is_used = True
            code_obj.save()
            login(request, user)
            return redirect('home')
        return render(request, "confirm_email.html", {"error": "Invalid or expired code"})
    return render(request, "confirm_email.html")





def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")






@login_required
@require_POST
def user_logout(request):
    logout(request)
    return redirect("home")






@login_required
@require_POST
def add_comment(request, article_id):
    article = get_object_or_404(Article,id=article_id,status="published" )
    text = request.POST.get("text", "").strip()
    Comment.objects.create( article=article, user=request.user, text=text)
    return redirect("article_detail", slug=article.slug)





def search_news(request):
    query = request.GET.get("q", "").strip()
    articles = Article.objects.none()
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query),
            status="published").select_related("category", "author")
    return render( request, "home.html", { "articles": articles, "categories": Category.objects.all(), "query": query,})
