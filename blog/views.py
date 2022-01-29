from django.shortcuts import render,get_object_or_404, redirect
from blog.models import Post,Comment
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)



def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submitted')
        else:
            messages.add_message(request,messages.ERROR,'your comment did not submitted')

    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts,pk=pid)
    post.counted_views=post.counted_views+1
    post.save()

    if X := Post.objects.filter(status=True, id__lt=post.id)[0:1]:
        prev_post = get_object_or_404(X)
    else:
        prev_post = post 
    if Y := Post.objects.filter(status=True, id__gt=post.id).order_by('id')[0:1]:
        next_post = get_object_or_404(Y)
    else:
        next_post = post


    if not post.login_require:
        comments =Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
        context = {'post':post,'comments':comments, 'form':form,'prev_post':prev_post,'next_post':next_post}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


def blog_category(request,cat_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name = cat_name)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if S:= request.GET.get('s'):
           posts = posts.filter(content__contains=S)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)