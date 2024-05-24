from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_users(request):
    url = 'http://dummyjson.com/users'
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        return JsonResponse(users, safe=False)
    else:
        return Response({'error': 'Failed to fetch users'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
