from django.db.models import Avg
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.filters import TitleFilter
from api.models.title import Title
from api.permissions import IsAdminOrReadOnly
from api.serializers.title import (TitleSerializerGet,
                                   TitleSerializerPost)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).order_by('name')

    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination

    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return TitleSerializerGet

        return TitleSerializerPost
