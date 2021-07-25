from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from api.models.genre import Genre
from api.permissions import IsAdminOrReadOnly
from api.serializers.genre import GenreSerializer
from api.viewsets import CreateDestroyReadOnlyCustom


class GenreViewSet(CreateDestroyReadOnlyCustom):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    lookup_field = 'slug'

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
