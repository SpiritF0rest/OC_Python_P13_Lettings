from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
    path('admin/', admin.site.urls),
    path('sentry-test/', views.sentry_test, name='sentry_test'),
]
