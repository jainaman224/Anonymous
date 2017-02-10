from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from djchan.APIPermissions import AuthToken
from realtime.models import User, Session
from realtime.serializers import UserSerializer


class RegistrationView(APIView):
    def post(self, request):
        if User.objects.filter(email=request.data['email']).exists():
            payload = {
                'result': False,
                'message': 'user already exists'
            }

            return Response(payload, status=status.HTTP_400_BAD_REQUEST)

        else:
            user = User.objects.create(**request.data)
            session_id = Session.generate_token(user_id=user.id)
            user_data = UserSerializer(instance=user).data

            payload = {
                'result': True,
                'message': 'User registered successfully',
                'user': user_data,
                'session_id': session_id
            }

            return Response(payload, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        user = User.objects.filter(**request.data).first()

        if user:
            session_id = Session.generate_token(user_id=user.id)

            user_data = UserSerializer(instance=user).data

            payload = {
                'result': True,
                'message': 'User login successfully',
                'user': user_data,
                'session_id': session_id
            }

            return Response(payload, status=status.HTTP_200_OK)

        else:
            payload = {
                'result': False,
                'message': 'Login credentials are wrong'
            }

            return Response(payload, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (AuthToken,)

    def get(self, request):
        Session.objects.filter(session_id=request.session.session_id).update(is_active=False)

        payload = {
            'result': True,
            'message': 'User logout successfully'
        }

        return Response(payload, status=status.HTTP_200_OK)
