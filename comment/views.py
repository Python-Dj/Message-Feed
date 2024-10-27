from django.shortcuts import render, redirect
from django.contrib import auth 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from account.models import User
from .models import Message, Comment, Like

from .forms import SignUpForm, MessageForm, CommentForm





def signUp(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already Sign Up!")
        return redirect("home")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            return redirect("login")
        else:
            return render(request, "signup.htm", {"form": form})
    form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already Logged In!")
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("feed")
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect("login")
    return render(request, "login.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")


@login_required(login_url="login")
def news_messages(request):
    if request.method == "POST":
        msgForm = MessageForm(request.POST)
        if msgForm.is_valid():
            message = msgForm.save(commit=False)
            message.user = request.user
            message.save()
            return redirect("feed")
    
    messages = Message.objects.all()
    return render(request, "home.html", {
        "messages": messages,
        "msgForm": MessageForm(),
        "cmtForm": CommentForm(),
    })


@login_required(login_url="login")
def comment(request, pk=None):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            message = Message.objects.get(pk=pk) 
            comment.message = message
            comment.user = request.user
            comment.save()
            return redirect("feed")
        

@login_required(login_url="login")
def delete_message(request, pk=None):
    message = Message.objects.get(pk=pk, user=request.user)
    message.delete()
    return redirect("feed")


@login_required(login_url="login")
def comment_likes(request, pk=None):
    comment = Comment.objects.get(pk=pk)
    obj, created = Like.objects.get_or_create(comment=comment, user=request.user)
    return redirect("feed")


@login_required(login_url="login")
def message_likes(request, pk=None):
    message = Message.objects.get(pk=pk)
    obj, created = Like.objects.get_or_create(message=message, user=request.user)
    return redirect("feed")