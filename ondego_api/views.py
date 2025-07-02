from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


@api_view()
def root_route(request):
    return Response({"message": "Welcome to ondego app API!"})


# Simple JWT logout view
@api_view(['POST'])
def logout_route(request):
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": "Error logging out."}, status=status.HTTP_400_BAD_REQUEST)
