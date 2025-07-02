from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import logout_route

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls')),

    # Simple JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Keep dj-rest-auth for user management
    path('api/dj-rest-auth/logout/', logout_route),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'api/dj-rest-auth/registration/',
        include('dj_rest_auth.registration.urls')
    ),
    path('api/', include('profiles.urls')),
    path('api/', include('events.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('joinings.urls')),
    path('api/', include('friends.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')
