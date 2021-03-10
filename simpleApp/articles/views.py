from django.shortcuts import render
from .models import Article

def articles_list_page(request):
	articles = Article.objects.all().order_by("id")
	return render(request, "articles/articles_list.html",
		{"articles":articles})