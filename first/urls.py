from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', myapp.views.main, name='main'),
    path('result/', myapp.views.result, name='result'),
    path('detail/<int:blog_id>', myapp.views.detail, name='detail'),
]
