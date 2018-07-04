django-rest-custom-exceptions
======================================

Custom exceptions for django rest framework

Compatibility
-------------

Works with :

  * Python 2.7, 3.4, 3.5, 3.6
  * Django >= 1.10
  * Django Rest Framework >= 3.5

Installation
------------

Install the package from pypi: ::

    pip install djangorestframework-custom-exceptions

Add the application in your django settings: ::

    INSTALLED_APPS = ('rest_framework_custom_exceptions',)

Configure your rest framework : ::

    REST_FRAMEWORK = {
        'EXCEPTION_HANDLER': 'rest_framework_custom_exceptions.exceptions.simple_error_handler'
    }

Example
-------

The simple error handler show exceptions like this : ::
    
    {
        "error": "Not found"
    }

