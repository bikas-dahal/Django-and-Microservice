from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework import permissions

from .serializers import NewsItemSerializer
from .models import NewsItem

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from news.forms import SuggestionForm


class SuggestionFormView(FormView):
    template_name = 'news/suggestion.html'
    form_class = SuggestionForm
    success_url = '/success/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    

class SuggestionSuccessView(TemplateView):
    template_name = 'news/suggestion_success.html'


class NewsItemApiView(APIView):
    permission_classes = [permissions.AllowAny]
    
    @method_decorator(cache_page(60 * 15))
    def get(self, request, format=None):
        news = NewsItem.objects.all().order_by('-time_stamp')
        serializer = NewsItemSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
