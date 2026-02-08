from django.urls import path

from iam.views.login_view import LoginView
from iam.views.refreshtoken_view import RefreshTokenView
from iam.views.membership_view import MembershipViewSet

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh-token')
]