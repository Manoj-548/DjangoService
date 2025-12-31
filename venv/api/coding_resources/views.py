from django.shortcuts import render, get_object_or_404
from .models import Category, Topic, CodeSnippet


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'coding_resources/category_list.html', {'categories': categories})


def topic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = category.topic_set.all()
    return render(request, 'coding_resources/topic_list.html', {'category': category, 'topics': topics})


def snippet_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    snippets = topic.codesnippet_set.all()
    return render(request, 'coding_resources/snippet_list.html', {'topic': topic, 'snippets': snippets})


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(CodeSnippet, id=snippet_id)
    return render(request, 'coding_resources/snippet_detail.html', {'snippet': snippet})
