from django.db import models

class DashboardApp(models.Model):
    name = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url_path = models.CharField(max_length=100, unique=True, help_text="URL path for this app (e.g., 'admin', 'coding-resources')")
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order in the main panel")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.display_name
