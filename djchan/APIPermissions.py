from rest_framework.permissions import BasePermission

from realtime.models import Session
from realtime.models import User


class AuthToken(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def check_token(self, request, headers):

        if 'HTTP_SESSIONID' in headers:

            session = Session.objects.filter(session_id=headers['HTTP_SESSIONID'],
                                             is_active=True).first()
            if session:
                request.session = session

                # fetching the user corresponding to the session id
                user = User.objects.get(pk=session.user_id)
                request.user = user

                return request
            else:
                return False
        else:
            return False

    def has_permission(self, request, view):
        return self.check_token(request, request.META)
