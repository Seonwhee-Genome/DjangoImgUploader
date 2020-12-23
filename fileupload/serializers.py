from fileupload.models import Imgmanager
from rest_framework import serializers


class ImgSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Imgmanager
        fields = ('image_name', 'image')