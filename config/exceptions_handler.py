from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError as drf_validation_error
from rest_framework.exceptions import PermissionDenied, APIException
from django.core.exceptions import ValidationError as django_validation_error
from django.db.utils import IntegrityError
from config.exceptions import BusinessRuleError, AuthenticationError


def custom_exception_handler(exc, context):
    print(type(exc))
    response = exception_handler(exc, context)


    if isinstance(exc, drf_validation_error):
        return Response(
            {
                "error": "Validation Error",
                "fields": exc.detail
            },
            status=status.HTTP_400_BAD_REQUEST
        )  
        
    if isinstance(exc, IntegrityError):
        return Response(
            {
                "error": "Database Integrity Error",
                "detail": exc.args
            },
            status=status.HTTP_400_BAD_REQUEST
        )  
    
    if isinstance(exc, AuthenticationError):
        return Response(
            {"error": str(exc)},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    if isinstance(exc, PermissionDenied):
        return Response(
            {
                "error": "Permission Denied",
                "detail": str(exc)
            },
            status=status.HTTP_403_FORBIDDEN
        )
        

    if isinstance(exc, BusinessRuleError):
        return Response(
            {"error": str(exc)},
            status=status.HTTP_400_BAD_REQUEST
        )
        
    if isinstance(exc, django_validation_error):
        return Response(
            {
                "error": "DJANGO Validation error",
                "detail": exc.args                
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        
    if isinstance(exc, APIException):
        return Response(
            {
                "error": str(exc.default_detail),
                "detail": str(exc)},
            status=exc.status_code
        )
    
    if response is not None:
        return Response(
            {
                "error": response.data,
            },
            status=response.status_code
        )
                
    print(str(exc))
    return Response(
        {"error": "Internal Server Error"}, 
        status=status.HTTP_500_INTERNAL_SERVER_ERROR 
    )