from __future__ import unicode_literals

from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import status, exceptions
from rest_framework.response import Response


def simple_error_handler(exc, *args):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's builtin `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['X-Throttle-Wait-Seconds'] = '%d' % exc.wait

        return Response({'error': exc.detail},
                        status=exc.status_code,
                        headers=headers)

    elif isinstance(exc, Http404):
        return Response({'error': 'Not found'},
                        status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        return Response({'error': 'Permission denied'},
                        status=status.HTTP_403_FORBIDDEN)

    # Note: Unhandled exceptions will raise a 500 error.
    return None
