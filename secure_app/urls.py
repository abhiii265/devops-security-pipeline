from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Loads the dashboard at the root URL
    path('', TemplateView.as_view(template_name='index.html')), 
]