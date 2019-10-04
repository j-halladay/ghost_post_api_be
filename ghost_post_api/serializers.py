# from rest_api.models import ShoeType, ShoeColor, Shoe, Manufacturer
from ghost_post_api.models import Message
from rest_framework import serializers


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['title', 'is_boast', 'like', 'text', 'created', 'updated']


# class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ShoeColor
#         fields = ['color_name']


# class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ShoeType
#         fields = ['style']


# class ShoeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Shoe
#         fields = ['brand_name', 'manufacturer', 'color',
#                   'material', 'shoe_type', 'fasten_type']


# class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Manufacturer
#         fields = ['name', 'website']
