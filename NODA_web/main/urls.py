from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('notes/', views.NotesPreview, name="notes"),
    path('register/', RegisterUser.as_view(), name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
