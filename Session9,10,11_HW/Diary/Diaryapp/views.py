from django.shortcuts import redirect, render
from .models import Diary, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/registration/login")
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_post = Diary.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    posts = Diary.objects.all()
    return render(request, 'list.html', {'posts':posts})

@login_required(login_url="/registration/login")
def detail(request, post_id):
    post = Diary.objects.get(id=post_id)
    print(type(post.author), "post.author")
    if request.method =='POST':
        content = request.POST['content']
        Comment.objects.create(
            post = post,
            content = content,
            author = request.user
        )
        return redirect('detail', post_id)
    return render(request, 'detail.html', {'post':post})

def edit(request, post_pk):
    post = Diary.objects.get(pk=post_pk)
    if request.method == "POST":
        Diary.objects.filter(pk=post_pk).update(
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

def signup(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST['password']
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "이미 아이디가 존재합니다"
            return render(request, "registration/signup.html", {"error":error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect("list")
    return render(request, "registration/signup.html")


def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            #return redirect("list")
            return redirect(request.GET.get("next","/"))

        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, "registration/login.html", {"error":error})

    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)
    return redirect("list")