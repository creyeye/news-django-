from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Post
from .forms import PostCreateForm, PostUpdateForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/post_list.html', {"posts": posts})


def index(request):
    posts = Post.objects.all()
    return render(request, 'app/index.html', {"posts": posts})
#lllll

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


def post_create(request):
    if request.method == 'POST':
        print(request.FILES)
        form = PostCreateForm(request.POST, request.FILES)  # Передаем request.FILES для обработки файлов
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostCreateForm()
    return render(request, 'app/post_create.html', {'form': form})


