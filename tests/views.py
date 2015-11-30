# -*- coding: utf-8 -*-

"""
"""
from django.core.exceptions import PermissionDenied 
from django.http import Http404 
from rest_framework import generics
from rest_framework.exceptions import ParseError

from . import models
from . import serializers


class ItemList(generics.ListAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

    def list(self, request, *args, **kwargs):
        if not request.query_params:
            raise ParseError(detail="Missing required fields")
        return super(ItemList, self).list(request, *args, **kwargs)


class NotItemList(ItemList):
    def list(self, request, *args, **kwargs):
        raise Http404


class ForbiddenItemList(ItemList):
    def list(self, request, *args, **kwargs):
        raise PermissionDenied
