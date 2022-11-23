from rest_framework import permissions, viewsets
from rest_framework.decorators import schema, action
from rest_framework.request import Request
from rest_framework.response import Response

from LokimoTest.LokimoTest.domain.ad_serializer import AdFullDTOSerializer
from LokimoTest.LokimoTest.models.AdModel import Ad
from LokimoTest.LokimoTest.services.AdSearch import general_filter_search, group_by_rooms
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
        result = general_filter_search(Ad, self.queryset, request)
        json_result = self.serializer_class(result, many=True).data
        return Response(json_result)

    @action(detail=False, methods=['get'])
    @schema(None)
    @wrap_error()
    def summary(self, request: Request):
        result = general_filter_search(Ad, self.queryset, request)
        selected_ads = self.serializer_class(result, many=True).data
        ad_summary_by_type = group_by_rooms(selected_ads)

        return Response(ad_summary_by_type.__dict__)
