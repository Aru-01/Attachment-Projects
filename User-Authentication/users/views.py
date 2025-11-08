from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from users.models import User
from users.serializers import (
    UserSerializer,
    RegisterSerializer,
    VerifyEmailSerializer,
    LoginSerializer,
    LogoutSerializer,
)
from users.permissions import IsSelfOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "Registration successful. Please verify your email.",
                "redirect": request.build_absolute_uri("/api/verify-email/"),
            },
            status=status.HTTP_201_CREATED,
        )


class VerifyEmailView(generics.GenericAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.save()
        return Response(
            {
                "message": "Email verified successfully.",
                "access": tokens["access"],
                "refresh": tokens["refresh"],
                "user": UserSerializer(tokens["user"]).data,
            }
        )


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSelfOrReadOnly]
    http_method_names = ["get", "patch", "head", "options"]  
    def get_permissions(self):
        if self.action == "partial_update":
            return [permissions.IsAuthenticated(), IsSelfOrReadOnly()]
        return [permissions.IsAuthenticated()]


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Logged out successfully."})
