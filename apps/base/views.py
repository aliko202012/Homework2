from django.shortcuts import render
from .models import News
from .serializers import NewsSeiralizers
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class NewsListAPI(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSeiralizers
class NewsCreateAPI(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSeiralizers
class NewsRetrieveAPI(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSeiralizers
class NewsUpdateAPI(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSeiralizers
class NewsDeleteAPI(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSeiralizers

class SettingsListCreateAPI(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSeiralizers


class SettingsMultiAPI(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSeiralizers