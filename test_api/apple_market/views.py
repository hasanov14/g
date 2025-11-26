from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Telephone
from .serializers import TelephoneSerializer


class TelephoneDetail(generics.RetrieveAPIView):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer


class TelephoneDelete(generics.DestroyAPIView):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer

class TelephoneList(APIView):
    def get(self, request):
        phones = Telephone.objects.all()
        serializer = TelephoneSerializer(phones, many=True)
        return Response(serializer.data)


class TelephoneCreate(APIView):
    def post(self, request):
        serializer = TelephoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TelephoneUpdate(APIView):
    def put(self, request, pk):
        phone = Telephone.objects.get(id=pk)
        serializer = TelephoneSerializer(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk):
        phone = Telephone.objects.get(id=pk)
        serializer = TelephoneSerializer(phone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TelephoneMixed(APIView):
    def get(self, request):
        phones = Telephone.objects.all()
        return Response(TelephoneSerializer(phones, many=True).data)

    def post(self, request):
        serializer = TelephoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
