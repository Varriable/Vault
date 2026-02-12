from django.urls import path, include

urlpatterns = [
    path('user/', include('users.urls')),
    path('secret/', include('secrets.urls')),
    path('log/', include('logs.urls')),

]
