from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.users.urls')),
    path('secret/', include('api.v1.secrets.urls')),
    path('log/', include('api.v1.logs.urls')),

]
