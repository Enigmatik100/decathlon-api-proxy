import json
from json import JSONDecodeError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import requests

from decathlon.settings import API_KEY, ACCESS_TOKEN, SPORT_CLASSIFIER_URL

headers = {
    'X-API-KEY': API_KEY,
    'Authorization': f"Bearer {ACCESS_TOKEN}"
}


class SportClassifierViewSet(ViewSet):

    def create(self, request, *args, **kwargs):
        try:
            response = requests.request("POST", SPORT_CLASSIFIER_URL, headers=headers, files=request.data)
            if response.status_code == 200:
                return Response(json.loads(response.text), status=status.HTTP_200_OK)
            return Response({"error": response.content, "success": False}, status=response.status_code)
        except JSONDecodeError as e:
            return Response({"error": str(e), "success": False}, status=status.HTTP_400_BAD_REQUEST)
