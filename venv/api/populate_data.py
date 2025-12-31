import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_dashboard.settings')
django.setup()

from coding_resources.models import Category, Topic, CodeSnippet

# Create sample categories
python_category = Category.objects.create(name='Python Basics', description='Fundamental concepts in Python programming')
web_category = Category.objects.create(name='Web Development', description='Web development with Python frameworks')

# Create sample topics
variables_topic = Topic.objects.create(category=python_category, title='Variables and Data Types', description='Understanding variables and data types in Python')
functions_topic = Topic.objects.create(category=python_category, title='Functions', description='Defining and using functions in Python')
django_topic = Topic.objects.create(category=web_category, title='Django Framework', description='Building web applications with Django')

# Create sample code snippets
CodeSnippet.objects.create(
    topic=variables_topic,
    title='Variable Assignment',
    code='name = "John"\nage = 25\nis_student = True',
    language='python'
)

CodeSnippet.objects.create(
    topic=functions_topic,
    title='Simple Function',
    code='def greet(name):\n    return f"Hello, {name}!"\n\nprint(greet("World"))',
    language='python'
)

CodeSnippet.objects.create(
    topic=django_topic,
    title='Django View',
    code='from django.shortcuts import render\n\ndef home(request):\n    return render(request, "home.html")',
    language='python'
)

print("Sample data populated successfully!")
