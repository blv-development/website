from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('submit/', views.handle_form_submission, name='handle_form_submission'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('visionaries/', include('devs_list.urls')),
    path('endorsements/', include('endorsements.urls'), name='endorsements'),
]