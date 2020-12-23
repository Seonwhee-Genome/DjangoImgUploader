from django.shortcuts import render

# Create your views here.
from .serializers import ImgSerializer
from .models import Imgmanager
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render, get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect



class ImgList(APIView):
    """
     Upload Image
    """
    
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Imgmanager.objects.all()
    serializer_class = ImgSerializer
    
    def create(self, request):
        file_uploaded = request.FILES.get('file')
        content_type = file_uploaded.content_type
        
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
    
    
    def get(self, request, *args, **kwargs):
        
        print(request.data)       
        print(request.FILES)

        return Response(status = status.HTTP_200_OK)



    def post(self, request, *args, **kwargs):
        
        img = request.FILES['image']
        def handle_uploaded_file(f):
            with open(os.path.join(os.getcwd(),"media", f.name),'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        handle_uploaded_file(img)
        
        return Response(status = status.HTTP_200_OK)
        