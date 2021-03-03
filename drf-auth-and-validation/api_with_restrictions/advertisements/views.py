from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend

class DeletePermission(BasePermission):

    def has_permission(self, request, view):
        p = str(request.get_full_path())[-2:-1]
        try:
            ad = view.queryset.get(id=p)
        except Advertisement.DoesNotExist:
            return False
        print(request.user, ad.creator)
        if request.user == ad.creator:
            return True
        else:
            return False


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.order_by("id").all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    def create(self, request, *args, **kwargs):
        orders = Advertisement.objects.filter(
            creator=request.user,
            status=AdvertisementStatusChoices.OPEN
            ).count()
        if orders > 10:
            return Response(
                {
                    "answer":"You have to much Active orders"
                },
                status.HTTP_403_FORBIDDEN
            )    
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "destroy"]:
            return [IsAuthenticated()]
        if self.action in ["destroy", "update", "partial_update"]:
            return[IsAuthenticated(), DeletePermission()]
        return []
