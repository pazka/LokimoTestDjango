from rest_framework import permissions, viewsets

from LokimoTest.LokimoTest.domain.ad_serializer import AdFullDTOSerializer
from LokimoTest.LokimoTest.services.ad_services import all_ads


class AdCRUD(viewsets.ModelViewSet):
    queryset = all_ads()
    serializer_class = AdFullDTOSerializer
    permission_classes = [permissions.AllowAny]
