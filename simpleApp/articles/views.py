from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def articles_list_page(request):
	articles = Article.objects.all().order_by("id")
	return render(request, "articles/articles_list.html",
		{"articles":articles})

def article_page(request,id):
	return HttpResponse(id)
