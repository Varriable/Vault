from django.urls import path
from .views import SecretCreateView, SecretEditView, SecretDeleteView, UserSecretsListView, SecretDetailView, SecretListView, SecretsByUserView   


urlpatterns = [
    path('list/', SecretListView.as_view(), name='secret-list'),
    path('create/', SecretCreateView.as_view(), name='secret-create'),
    path('<int:secret_id>/edit/', SecretEditView.as_view(), name='secret-edit'),
    path('<int:secret_id>/delete/', SecretDeleteView.as_view(), name='secret-delete'),
    path('my-secrets/', UserSecretsListView.as_view(), name='user-secrets-list'),
    path('<int:secret_id>/', SecretDetailView.as_view(), name='secret-detail'),
    path('by-user/<int:user_id>/', SecretsByUserView.as_view(), name='secrets-by-user'),
    
]
