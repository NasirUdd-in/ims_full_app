from rest_framework.decorators import api_view
from .serializers import  RegisterSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Register API
@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "User Created Successfully. Now perform Login to get your token",
        })
    return Response(serializer.errors, status=400)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)

        # Blacklist the refresh token to invalidate it
        token.blacklist()

        # Clear the user session
        session_key = request.session.session_key
        if session_key:
            # Retrieve the session object
            session = Session.objects.get(session_key=session_key)
            session_data = session.get_decoded()

            # Perform session cleanup actions (example: clear specific keys or all keys)
            session_data.pop('your_key', None)  # Remove a specific key from session data
            session_data.clear()  # Clear all keys from session data

            # Save the modified session data
            session.update({session.session_key: session_data})

        # Perform any additional logout-related actions here
        logout(request)

        return Response({"detail": "Logout successful."})
    except TokenError:
        return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
