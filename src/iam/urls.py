from django.urls import path

from iam.views.login_view import LoginView
from iam.views.refreshtoken_view import RefreshTokenView
from iam.views.confirm_email_view import ConfirmationEmailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh-token'),
    path('confirm-email', ConfirmationEmailView.as_view(), name='confirm-email'),
]