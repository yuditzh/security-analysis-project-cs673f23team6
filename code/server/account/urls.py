from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt import views as jwt_views

from .views import CustomTokenObtainPairView, AccountView, LogoutView
from .auth.api import RegisterAccountView, ChangePasswordView
from .views import CustomTokenObtainPairView, AccountView, ForgotPasswordView


urlpatterns = [
    # User Auth URLS
    path("register", RegisterAccountView.as_view()),
    path("login", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("logout", LogoutView.as_view(), name="auth_logout"),
    path("changepass", ChangePasswordView.as_view(), name="change_password"),
    path('password-reset', ForgotPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # Account Info URL
    path("user", AccountView.as_view()),
    ]


