from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Post, Comment, CustomUser


# to create token for jwt
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.user.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_by', 'created_date')


class ProfileSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    comment_by = serializers.ReadOnlyField(source='comment_by.user.username')

    class Meta:
        model = Comment
        fields = '__all__'
