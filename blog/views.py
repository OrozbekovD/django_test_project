from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from blog.models import Category, Post, Author, Comments, User


def index(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    users = User.objects.all()
    try:
        category_fan = Category.objects.get(title='Фантастика')
    except ObjectDoesNotExist:
        raise ValueError('Такой категории не существует!')
    return render(request, 'index.html', {'categories': categories, 'fan': category_fan, 'authors': authors})

    params = {'categories': categories,
              'fan': category_fan, 'authors': authors,
              'users': users, 'comments': com}
    return render(request, 'index.html', params)


def category(request, pk):
    posts = Post.objects.filter(category_id=pk)
    return render(request, 'category.html', locals())


def author(request, pk):
    posts = Post.objects.filter(author_id=pk)
    params = {'posts': posts}
    return render(request, 'posts_by_author.html', params)


def comments(request, pk):
    _comments = Comments.objects.filter(user_id=pk)
    return render(request, 'comments.html', {'comments': comments})
    com_list = []
    for c in comments():
        us = User.objects.filter(comments_id=c.id)
        if us:
            com_list.append(c.id)
    com = comments.filter(id__in=com_list)