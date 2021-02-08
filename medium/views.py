# from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from medium.models import Article
from medium.request import find_article
from medium.serializers import ApiCreate


@api_view(["GET"])
def api_view(request):
    find_article()
    articles = Article.objects.all()
    serializer = ApiCreate(articles, many=True)
    return Response(
        serializer.data, status=HTTP_200_OK
    )
