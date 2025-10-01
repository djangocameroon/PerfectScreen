from django.shortcuts import render
from django.core.paginator import Paginator
from .models import SocialPost


def home(request):
    all_posts = SocialPost.objects.all()
    hero_posts = all_posts[:4]

    posts_list = all_posts[4:]
    paginator = Paginator(posts_list, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'hero_posts': hero_posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/home.html', context)


def gallery(request):
    all_posts = SocialPost.objects.all()
    paginator = Paginator(all_posts, 16)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/gallery.html', context)
