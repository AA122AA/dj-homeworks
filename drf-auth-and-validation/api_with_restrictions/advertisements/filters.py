from django_filters import rest_framework as filters
from django_filters.filters import CharFilter, ChoiceFilter, DateFromToRangeFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    # creator = 

    class Meta:
        model = Advertisement
        fields=("status", "created_at", "creator")
