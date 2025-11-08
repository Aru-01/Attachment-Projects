from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.utils.email import send_otp_email
import random


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "address", "phone", "occupation"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "address",
            "phone",
            "occupation",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            address=validated_data.get("address", ""),
            phone=validated_data.get("phone", ""),
            occupation=validated_data.get("occupation", ""),
            is_active=False,
        )

        otp = str(random.randint(100000, 999999))
        user.email_otp = otp
        user.otp_created_at = timezone.now()
        user.save()

        send_otp_email(user.email, otp)

        return user


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get("email")
        otp = attrs.get("otp")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        if user.email_otp != otp:
            raise serializers.ValidationError("Invalid OTP.")

        if timezone.now() - user.otp_created_at > timezone.timedelta(minutes=10):
            raise serializers.ValidationError("OTP expired.")

        attrs["user"] = user
        return attrs

    def save(self):
        user = self.validated_data["user"]
        user.is_active = True
        user.email_otp = ""
        user.save()

        refresh = RefreshToken.for_user(user)
        return {
            "user": user,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.is_active:
            raise serializers.ValidationError("Email not verified.")
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError("Invalid token")
