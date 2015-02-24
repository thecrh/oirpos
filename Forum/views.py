# -*- coding: utf-8 -*-
from django.shortcuts import render
from Forum.models import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from Forum.forms import *
from Forum import models as m
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.template.loader import get_template
from django.template import RequestContext

# Create your views here.

def forum(request):
    """Forum listing."""
    topics = Topic.objects.all().order_by('-created')
    return render(request, 'forum/forum.html', {'topics': topics})

def about(request):
    """About listing"""
    return render(request, 'forum/about.html')

def topic(request, topic_id):
    try:
        topics = Topic.objects.get(id=topic_id)
    except ObjectDoesNotExist:
        raise Http404
    posts = Post.objects.all().filter(topic=topic_id).order_by('-created')
    return render(request, 'forum/topic.html', {'topics': topics, 'posts': posts})

def new(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = TopicForm(request.POST)
            if form.is_valid():
                tmptopic = form.save(commit=False)
                tmptopic.creator = User.objects.get(username=request.user.username)
                tmptopic.save()
                return redirect('/topic/' + str(tmptopic.id))

        form = TopicForm
        return render(request, 'forum/newtopic.html', {'form': form})
    else:
        return HttpResponseRedirect("/login")

def reply(request, topic_id):
    if request.user.is_authenticated():
        try:
            _topic = Topic.objects.get(id=topic_id)
        except ObjectDoesNotExist:
            raise Http404

        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                print topic_id
                tmppost = form.save(commit=False)
                tmppost.creator = User.objects.get(username=request.user.username)
                tmppost.topic = Topic.objects.get(id=topic_id)
                tmppost.save()
                return redirect('/topic/' + topic_id)

        form = PostForm
        return render(request, 'forum/reply.html', {'topic': _topic, 'form': form})
    else:
        return HttpResponseRedirect("/login")

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

def register_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                  username=form.cleaned_data['username'],
                  password=form.cleaned_data['password1']
            )
            user.save()
            template = get_template("registration/register_success.html")
            variables = RequestContext(request,{'username':form.cleaned_data['username']})
            output = template.render(variables)
            return HttpResponse(output)
    else:
        form = RegisterForm()
    template = get_template("registration/register.html")
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)
