from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostCreateForm, PostUpdateForm, UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/post_list.html', {"posts": posts})


def index(request):
    posts = Post.objects.all()
    return render(request, 'app/index.html', {"posts": posts})


def post_detail(request, pk):

    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_list')
        else:
            print(form.errors)
    form = PostUpdateForm(instance=post)

    return render(
        request,
        'app/post_detail.html',
        {
            'post': post,
            'form': form
        })


@login_required(login_url='/login/')
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                user=request.user,
                title=request.POST['title'],
                description=request.POST['description'],
                file=request.FILES['file'],
                preview=request.FILES['preview'],
            )
            post.save()
            return redirect('index')
    else:
        form = PostCreateForm()
    return render(request, 'app/post_create.html', {'form': form})


def post_delete(pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('post_list')


def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserRegisterForm()

    return render(
        request,
        'app/sign_up.html',
        {
            'form': form
        }
    )


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {'form': form})


def user_logout(request):

    logout(request)

    return redirect('index')
