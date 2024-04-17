from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import status
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .auth.serializer import AccountSerializer
from .models import CustomUser

class CustomTokenObtainPairView(TokenObtainPairView):
	def post(self, request, *args, **kwargs):
		user = CustomUser.objects.get(email=request.data["email"])
		if not user.is_active:
			return Response({'message': 'User is not active.'}, status=status.HTTP_401_UNAUTHORIZED)
		return super().post(request, *args, **kwargs)
	
class AccountView(APIView):
	permission_classes = (IsAuthenticated,)
	parser_classes = [JSONParser, MultiPartParser, FormParser]

	def get(self, request):
		serializer = AccountSerializer(request.user, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(APIView):
	permission_classes = (IsAuthenticated,)
	parser_classes = [JSONParser, MultiPartParser, FormParser]

	def post(self, request):
		try:
			refresh_token = request.data["refresh_token"]
			token = RefreshToken(refresh_token)
			# Refresh Token doesn't get destroyed, block it
			token.blocklist()

			return Response(status=status.HTTP_205_RESET_CONTENT)
		except Exception as e:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(SuccessMessageMixin, PasswordResetView):
	"""
	Ref: https://dev.to/earthcomfy/django-reset-password-3k0l
	"""
	template_name = 'password_reset_form.html'
	email_template_name = 'password_reset_email.html'
	subject_template_name = 'password_reset_subject.txt'
	success_message = "We've emailed you instructions for setting your password, " \
						"if an account exists with the email you entered. You should receive them shortly." \
						" If you don't receive an email, " \
						"please make sure you've entered the address you registered with, and check your spam folder."
	success_url = "http://localhost:3000/"
