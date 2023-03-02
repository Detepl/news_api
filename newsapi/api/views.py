from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from .models import News
from rest_framework.views import APIView
from .serializers import NewsSerializer


# class NewsAPIview(generics.ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


class NewsAPIview(APIView):

    def get(self, request):
        inf = News.objects.all()
        return Response({"title": NewsSerializer(inf, many=True).data})

    def get_queryset(self):
        user = self.request.user
        return News.objects.filter(purchaser=user)

    def post(self, request):
        serializer = NewsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT not allowed"})

        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = NewsSerializer(data = request.data, instance = instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
