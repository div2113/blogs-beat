from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  #generate access & refresh tokens
    TokenRefreshView,     #refresh access token
    TokenVerifyView       #verify if token is valid    
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

#define swagger schema view with JWT security

schema_view=get_schema_view(
    openapi.Info(
        title="Blogbeats API",
        default_version='v1',
        description='API for Blogbeats platform',
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@blogbeats.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=(JWTAuthentication,),

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('user.urls')),
    path('blogs/',include("blog.urls")),
    path('likes/',include("like.urls")),
    path('comments/',include("comments.urls")),
    path('api/token/',TokenObtainPairView.as_view()),       #get access & refresh token
    path('api/token/refresh/',TokenRefreshView.as_view()),  #get new access token
    path('api/token/verify',TokenVerifyView.as_view()),     #verify if token is valid
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
