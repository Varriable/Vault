from django.urls import path
from .views import OtpApiView, VerifyOtpApiView


urlpatterns = [
    path('send/', OtpApiView.as_view(), name='send-otp'),
    path('verify/', VerifyOtpApiView.as_view(), name='verify-otp'),
]