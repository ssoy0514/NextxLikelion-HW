from django.shortcuts import redirect, render
from .models import Diary, Comment
# Create your views here.

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_post = Diary.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    posts = Diary.objects.all()
    return render(request, 'list.html', {'posts':posts})

def detail(request, post_id):
    post = Diary.objects.get(id=post_id)
    if request.method =='POST':
        content = request.POST['content']
        Comment.objects.create(
            post = post,
            content = content
        )
        return redirect('detail', post_id)
    return render(request, 'detail.html', {'post':post})

def edit(request, post_pk):
    post = Diary.objects.filter(pk=post_pk)
    if request.method == "POST":
        post.update(
            title=request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', post_pk)
    return render(request, 'edit.html', {'post':post})

def delete(request, post_pk):
    post = Diary.objects.get(pk=post_pk)
    post.delete()

    return redirect('list')

def delete_comment(request, post_pk, comment_pk):
    comment= Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)