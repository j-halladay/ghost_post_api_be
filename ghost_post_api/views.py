# from django.contrib.auth.models import User, Group
# from rest_api.models import ShoeType, ShoeColor, Shoe, Manufacturer
# from rest_api.serializers import ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer, ManufacturerSerializer
from rest_framework import viewsets
from ghost_post_api.models import Message
from ghost_post_api.serializers import MessageSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
# from rest_framework.views import UpdateAPIView
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(methods=['post'], detail=True)
    def upvote(self, request, pk):
        m = Message.objects.get(pk=pk)
        m.like += 1
        m.save()
        return JsonResponse({'status': '200'})

    @action(methods=['post'], detail=True)
    def downvote(self, request, pk):
        m = Message.objects.get(pk=pk)
        m.like -= 1
        m.save()
        return JsonResponse({'status': '200'})
# class ShoeTypeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = ShoeType.objects.all()
#     serializer_class = ShoeTypeSerializer


# class ShoeColorViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = ShoeColor.objects.all()
#     serializer_class = ShoeColorSerializer


# class ShoeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Shoe.objects.all()
#     serializer_class = ShoeSerializer


# class ManufacturerViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Manufacturer.objects.all()
#     serializer_class = ManufacturerSerializer
