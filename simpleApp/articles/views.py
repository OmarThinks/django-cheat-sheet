from django.shortcuts import render


def articles_list_page(request):
	return render(request, "articles/articles_list.html")