from rest_framework import permissions, viewsets
from rest_framework.decorators import schema, action
from rest_framework.request import Request
from rest_framework.response import Response

from LokimoTest.LokimoTest.domain.ad_serializer import AdFullDTOSerializer
from LokimoTest.LokimoTest.models.AdModel import Ad
from LokimoTest.LokimoTest.services.AdSearch import apply_generic_query_filter, apply_ad_filter_radius
from LokimoTest.LokimoTest.services.ad_services import all_ads
from LokimoTest.LokimoTest.services.error_wrapper import wrap_error


class AdCRUD(viewsets.ModelViewSet):
    queryset = all_ads()
    serializer_class = AdFullDTOSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    @schema(None)
    @wrap_error()
    def search(self, request: Request):
        result = apply_generic_query_filter(Ad, self.queryset, request.GET)
        result = apply_ad_filter_radius(
            result,
            float(request.GET['x']) if 'x' in request.GET else None,
            float(request.GET['y']) if 'y' in request.GET else None,
            float(request.GET['r']) if 'r' in request.GET else 500,
        )

        json_result = self.serializer_class(result, many=True).data
        return Response(json_result)
