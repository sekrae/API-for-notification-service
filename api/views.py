from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Mailing, Client, Message, Tag
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer, TagSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MailingStatisticsAPIView(APIView):

    @staticmethod
    def get(request):
        mailing_count = Mailing.objects.count()

        sent_messages_count = Message.objects.filter(send_status='Доставлено').count()
        in_progress_messages_count = Message.objects.filter(send_status='В процессе').count()
        not_sent_messages_count = Message.objects.filter(send_status='Не отправлено').count()

        statistics = {
            'mailing_count': mailing_count,
            'sent_messages_count': sent_messages_count,
            'in_progress_messages_count': in_progress_messages_count,
            'not_sent_messages_count': not_sent_messages_count,
        }

        return Response(statistics)