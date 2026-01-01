from django.shortcuts import render, get_object_or_404
from .models import Category, Topic, CodeSnippet


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'coding_resources/category_list.html', {'categories': categories})


def topic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    return render(request, 'coding_resources/topic_list.html', {'category': category, 'topics': topics})


def snippet_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    snippets = CodeSnippet.objects.filter(topic=topic)
    return render(request, 'coding_resources/snippet_list.html', {'topic': topic, 'snippets': snippets})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category
import json


def list_categories(request):
    categories = Category.objects.filter(is_active=True).values(
        "id", "name", "description"
    )
    return JsonResponse({"categories": list(categories)})


@csrf_exempt
def create_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        category = Category.objects.create(
            name=data["name"],
            description=data.get("description", "")
        )
        return JsonResponse({
            "id": category.id,
            "name": category.name
        })
