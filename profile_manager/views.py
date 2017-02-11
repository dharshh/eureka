#from rest_framework import viewsets
from .models import Provider
from .models import Category
from .models import Subcategory
from .serializers import ProviderSerializer
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json

# class ProviderViewSet(viewsets.ModelViewSet):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer


@api_view(['GET', 'POST'])
def provider_list(request):
    """
    List all providers, or create a new provider.
    """
    if request.method == 'GET':
        if 'city_id' in request.GET:
            if 'locality_id' in request.GET:
                if 'category_id' in request.GET:
                    published = request.GET.get('published', None)
                    city_id = request.GET.get('city_id', None)
                    locality_id = request.GET.get('locality_id', None)
                    category_id = request.GET.get('category_id', None)
                    snippets = Provider.objects.filter(published=published).filter(city_id=city_id).\
                        filter(locality_id=locality_id).filter(category_id=category_id)
                elif 'subcategory_id' in request.GET:
                    published = request.GET.get('published', None)
                    city_id = request.GET.get('city_id', None)
                    locality_id = request.GET.get('locality_id', None)
                    subcategory_id = request.GET.get('subcategory_id', None)
                    snippets = Provider.objects.filter(published=published).filter(city_id=city_id).\
                        filter(locality_id=locality_id).filter(subcategory_id=subcategory_id)
                else:
                    published = request.GET.get('published', None)
                    city_id = request.GET.get('city_id', None)
                    locality_id = request.GET.get('locality_id', None)
                    snippets = Provider.objects.filter(published=published).filter(city_id=city_id).\
                        filter(locality_id=locality_id)
            elif 'category_id' in request.GET:
                published = request.GET.get('published', None)
                city_id = request.GET.get('city_id', None)
                category_id = request.GET.get('category_id', None)
                snippets = Provider.objects.filter(published=published).filter(city_id=city_id)\
                    .filter(category_id=category_id)
            elif 'subcategory_id' in request.GET:
                published = request.GET.get('published', None)
                city_id = request.GET.get('city_id', None)
                subcategory_id = request.GET.get('category_id', None)
                snippets = Provider.objects.filter(published=published).filter(city_id=city_id)\
                    .filter(subcategory_id=subcategory_id)
            else:
                city_id = request.GET.get('city_id', None)
                published = request.GET.get('published', None)
                snippets = Provider.objects.filter(published=published).filter(city_id=city_id)
        else:
            snippets = Provider.objects.filter(published=1)
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


@api_view(['GET'])
def category_list(request):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        published = request.GET.get('published', None)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            # Ignore queries shorter than length 3
            if len(value) > 2:
                model_results = Category.objects.filter(category_name__icontains=value).filter(published=1)
                results = [ x.category_name for x in model_results ]
    json1 = json.dumps(results)
    return HttpResponse(json1)

