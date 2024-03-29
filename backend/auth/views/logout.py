from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import viewsets, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class LogoutViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')
        if not refresh:
            raise ValidationError({
                'detail': 'Refresh token is required.'
            })

        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            raise ValidationError({
                'detail': "Refresh token is invalid."
            })
