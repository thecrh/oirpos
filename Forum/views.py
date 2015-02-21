from django.shortcuts import render
from Forum.models import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from Forum.forms import *
from Forum import models as m
from django.http import HttpResponseRedirect
# Create your views here.


def test(request):
    return render_to_response('test.html', {'imie': 'Piotr', 'framework': 'django'})


def forum(request):
    """Forum listing."""
    topics = Topic.objects.all().order_by('created')
    return render(request, 'forum/forum.html', {'topics': topics})


def topic(request, topic_id):
    topics = Topic.objects.get(id=topic_id)
    posts = Post.objects.all().filter(topic=topic_id)
    return render(request, 'forum/topic.html', {'topics': topics, 'posts': posts})


def new(request):
    form = TopicForm
    return render(request, 'forum/newtopic.html', {'form': form})


def reply(request, topic_id):
    return render(request, 'forum/reply.html', {'topic_id': topic_id})


def new_topic(request):
    if request.method == 'GET':
        form = TopicForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = TopicForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            tmp_topic = m.Topic.objects.create(content=content, created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail', kwargs={'topic_id': topic.id}))

    return render(request, '/forum/newtopic.html', {
        'form': form,
    })

