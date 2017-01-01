#from rest_framework import viewsets
from .models import Provider
from .serializers import ProviderSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# class ProviderViewSet(viewsets.ModelViewSet):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer


@api_view(['GET', 'POST'])
def provider_list(request, format=None):
    """
    List all providers, or create a new provider.
    """
    if request.method == 'GET':
        snippets = Provider.objects.all()
        serializer = ProviderSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def provider_detail(request, id, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        provider_id = Provider.objects.get(id=id)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProviderSerializer(provider_id)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProviderSerializer(provider_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        provider_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

