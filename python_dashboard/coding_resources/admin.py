from django.contrib import admin
from .models import Category, Topic, CodeSnippet

# Customize admin site
admin.site.site_header = "Python Coding Resources Dashboard"
admin.site.site_title = "Dashboard Admin"
admin.site.index_title = "Welcome to the Dashboard Admin"

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(CodeSnippet)
