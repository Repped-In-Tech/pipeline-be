"""View module for handling requests about techies"""
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from pipelineapi.models import Techie
from pipelineapi.serializers import TechieSerializer

from .pagination import CustomPagination


class TechieView(mixins.ListModelMixin, GenericViewSet):
    """
    list:
    Return a list of all the existing techies.
    """
    pagination_class = CustomPagination
    serializer_class = TechieSerializer
    queryset = Techie.objects.all()
