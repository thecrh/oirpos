from django.shortcuts import render
from Forum.models import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from Forum.forms import *
from Forum import models as m
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.


def forum(request):
    """Forum listing."""
    topics = Topic.objects.all().order_by('created')
    return render(request, 'forum/forum.html', {'topics': topics})


def about(request):
    """About listing"""
    return render(request, 'forum/about.html')


def topic(request, topic_id):
    topics = Topic.objects.get(id=topic_id)
    posts = Post.objects.all().filter(topic=topic_id)
    return render(request, 'forum/topic.html', {'topics': topics, 'posts': posts})


def new(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        tmptopic = form.save(commit=False)
        tmptopic.creator = User.objects.get(username='windoo')  # do poprawki dodac logowanie
        tmptopic.save()
        return redirect('/')
    else:
        form = TopicForm
        return render(request, 'forum/newtopic.html', {'form': form})


def reply(request, topic_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print topic_id
        tmppost = form.save(commit=False)
        tmppost.creator = User.objects.get(username='windoo')  # do poprawki dodac logowanie
        tmppost.topic = Topic.objects.get(id=topic_id)
        tmppost.save()
        return redirect('/topic/' + topic_id + '/')
    else:
        form = PostForm
        return render(request, 'forum/reply.html', {'topic_id': topic_id, 'form': form})
