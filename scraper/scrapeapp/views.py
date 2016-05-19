from django.shortcuts import render, get_object_or_404

from .models import RedditLinks


def index(request):
	latest_item_list = RedditLinks.objects.order_by('-pub_date')
	context = {'latest_item_list': latest_item_list}
	return render(request, 'scrapeapp/index.html', context)


def detail(request, item_id):
	item = get_object_or_404(RedditLinks, pk=item_id)
	return render(request, 'scrapeapp/detail.html', {'item': item})