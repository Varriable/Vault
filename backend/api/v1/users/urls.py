from django.urls import path
from .views import LoginView, RefreshView, LogoutView ,UserCreateView, UserEditView, UserDeleteView, UserListView, MeView, UserDetailView


urlpatterns = [
    path('login/', LoginView.as_view(), name='user-login'),
    path('refresh/', RefreshView.as_view(), name='token-refresh'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:user_id>/edit/', UserEditView.as_view(), name='user-edit'),
    path('<int:user_id>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('me/', MeView.as_view(), name='user-me'),
    path('<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
]
