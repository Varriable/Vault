from django.urls import path
from .views import LogCreateView, UserLogsView, LogDetailView, LogDeleteView, ClearUserLogsView, AllLogsView, LogsByActionView

urlpatterns = [
    path('create/', LogCreateView.as_view(), name='log-list-create'),
    path('user/<int:user_id>/', UserLogsView.as_view(), name='user-logs'),
    path('<int:log_id>/', LogDetailView.as_view(), name='log-detail'),
    path('<int:log_id>/delete/', LogDeleteView.as_view(), name='log-delete'),
    path('user/<int:user_id>/clear/', ClearUserLogsView.as_view(), name='clear-user-logs'),
    path('all/', AllLogsView.as_view(), name='all-logs'),
    path('action/<str:action>/', LogsByActionView.as_view(), name='logs-by-action'),
]